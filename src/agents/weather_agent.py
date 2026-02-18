import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# ---------------- OUTPUT FORMAT CLASS ----------------

class OutputStep:
    def __init__(self, step, content, tool=None):
        self.step = step
        self.content = content
        self.tool = tool

    def to_dict(self):
        data = {
            "step": self.step,
            "content": self.content
        }
        if self.tool:
            data["tool"] = self.tool
        return data

# ---------------- WEATHER TOOL ----------------

def get_weather(city):
    r = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5)
    r.raise_for_status()
    d = r.json()["current_condition"][0]
    return {
        "city": city.title(),
        "condition": d["weatherDesc"][0]["value"],
        "temp_c": d["temp_C"],
        "humidity": d["humidity"]
    }

# ---------------- PLANNER ----------------

def planner(query):
    r = client.chat.completions.create(
        model="google/gemma-3-4b-it",
        response_format={"type":"json_object"},
        messages=[
            {"role":"system","content":
             "Return JSON only: {action: weather|llm, city: string}"},
            {"role":"user","content":query}
        ]
    )
    return json.loads(r.choices[0].message.content)

# ---------------- MAIN AGENT ----------------

def main():
    while True:
        q = input("> ")
        if q.lower() in {"exit","quit"}:
            break

        plan = planner(q)
        steps = []

        if plan["action"] == "weather":
            steps.append(OutputStep("START", f"User asks weather in {plan['city']}."))
            steps.append(OutputStep("PLAN", "Detect weather intent."))
            steps.append(OutputStep("PLAN", f"Extract city = {plan['city']}."))
            steps.append(OutputStep("PLAN", "Call weather tool.", tool="wttr.in"))

            data = get_weather(plan["city"])

            steps.append(OutputStep(
                "OUTPUT",
                f"Weather in {data['city']} is {data['condition']}, {data['temp_c']}°C."
            ))
            steps.append(OutputStep("END", "Return result to user."))

            print(json.dumps([s.to_dict() for s in steps], indent=2))

            print("\nFinal Answer:")
            print(
                f"The current weather in {data['city']} is "
                f"{data['condition']}, {data['temp_c']}°C "
                f"with humidity {data['humidity']}%.\n"
            )

        else:
            r = client.chat.completions.create(
                model="google/gemma-3-4b-it",
                messages=[{"role":"user","content":q}]
            )
            print(r.choices[0].message.content)

if __name__ == "__main__":
    main()
