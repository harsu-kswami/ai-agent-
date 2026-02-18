# from fastapi import FastAPI, Body
# from ollama import Client

# app = FastAPI()

# client = Client(
#     host="http://localhost:11434",
# )

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.post("/chat")
# def chat(message: str = Body(..., embed=True)):
#     response = client.chat(
#         model="gemma:2b",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": message},
#         ],
#     )

#     return {"response": response["message"]["content"]}


from transformers import pipeline

pipe = pipeline("image-text-to-text", model= "google/gemma-3-4b-it")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "input_text", "url": "https://www.dreamstime.com/photos-images/candy-cow.html"},
            {"type": "text", "text": "what animal is on this candy?"}
        ]
    }
]
pipe(text=messages)