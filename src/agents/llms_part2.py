# # implemening a custom tokenizer in python 

# import tiktoken

# enc = tiktoken.encoding_for_model("gpt-4o")
# text = "Hello, how are you doing today?"
# tokens = enc.encode(text)


# # [13225, 11, 1495, 553, 481, 5306, 4044, 30]
# print(tokens)

# decoded = enc.decode([13225, 11, 1495, 553, 481, 5306, 4044, 30])
# print(decoded)


# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1"
# )
# x = "You are a mathematical solver. if some query not related to math, then reply with 'I can only solve mathematical problems.' "
# response = client.chat.completions.create(
#     model="openai/gpt-4o-mini",
#     max_tokens=256,
#     messages=[
#         {"role": "system", "content": x},
#         {"role": "user", "content": "What is the capital of France?"}
#     ]
# )

# print(response.choices[0].message.content)



# zero shot prompting :- directly giving inst to the model



# few shot prompting :- giving some examples to the model and then asking the question

# chain of thought prompting :- giving some examples to the model and then asking the question but also asking the model to explain the answer step by step

# import os
# import json
# from dotenv import load_dotenv
# from openai import OpenAI

# # Load env variables
# load_dotenv()

# # Create client (OpenRouter)
# client = OpenAI(
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1"
# )

# # ================================
# # SYSTEM PROMPT
# # ================================

# SYSTEM_PROMPT = """
# You are a mathematical solver.

# If the user asks anything NOT related to math, reply exactly:
# "I can only solve mathematical problems."

# You must work in steps:
# START -> PLAN -> OUTPUT -> END

# --------------------
# RULES
# --------------------
# - Always return a JSON ARRAY.
# - Each item must be a JSON object.
# - Each object must contain:
#   - step
#   - content
# - Do not return plain text.
# - Do not explain outside JSON.
# - Follow order strictly.

# --------------------
# OUTPUT FORMAT
# --------------------
# [
#   {"step":"START","content":"string"},
#   {"step":"PLAN","content":"string"},
#   {"step":"OUTPUT","content":"string"},
#   {"step":"END","content":"string"}
# ]

# --------------------
# EXAMPLE
# --------------------
# User Input:
# Solve 2+2*4/8

# Assistant Output:
# [
#   {"step":"START","content":"User wants to solve expression 2+2*4/8."},
#   {"step":"PLAN","content":"Apply BODMAS rule."},
#   {"step":"PLAN","content":"First compute 4/8."},
#   {"step":"PLAN","content":"Then multiply 2*0.5."},
#   {"step":"PLAN","content":"Then add 2+1."},
#   {"step":"OUTPUT","content":"Final calculation result is 3."},
#   {"step":"END","content":"Answer is 3."}
# ]
# """

# # ================================
# # CALL MODEL
# # ================================

# response = client.chat.completions.create(
#     model="openai/gpt-4o-mini",
#     response_format={"type": "json_object"},
#     max_tokens=300,
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Solve 2+2*4/8"}, 
#         # manulally add the instruction to return json array, because response_format only works for single json object, not for array of json objects
#         {'response': [{'step': 'START', 'content': 'User wants to solve expression 2+2*4/8.'}, {'step': 'PLAN', 'content': 'Apply BODMAS rule.'}, {'step': 'PLAN', 'content': 'First compute 4/8.'}, {'step': 'PLAN', 'content': 'Then multiply 2*0.5.'}, {'step': 'PLAN', 'content': 'Then add 2+1.'}, {'step': 'OUTPUT', 'content': 'Final calculation result is 3.'}, {'step': 'END', 'content': 'Answer is 3.'}]}
#     ]
# )

# # ================================
# # PARSE + PRINT
# # ================================

# raw = response.choices[0].message.content
# data = json.loads(raw)

# if isinstance(data, dict):
#     data = [data]

# for step in data:
#     print(step)


# prompt style 
# alpaca prompt style :-
### instruction: <system_prompt>\n
### input: <user_input>\n
### response: \n

# response = client.chat.completions.create(
#     model="openai/gpt-4o-mini",
#     max_tokens=300,
#     messages=[
#         {
#             "role": "user",
#             "content": f"""
# ### Instruction:
# You are a mathematical solver.
# Follow START -> PLAN -> OUTPUT -> END.
# Return strictly a JSON array with fields: step, content.

# ### Input:
# Solve 2+2*4/8

# ### Response:
# """
#         }
#     ]
# )


# chatml prompt style :-
# {
#   "role": "system" | "user" | "assistant",
#   "content": "string"
# }

# response = client.chat.completions.create(
#     model="openai/gpt-4o-mini",
#     max_tokens=300,
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a mathematical solver. Follow START -> PLAN -> OUTPUT -> END. Return JSON array only."
#         },
#         {
#             "role": "user",
#             "content": "Solve 2+2*4/8"
#         }
#     ]
# )

# inst style prompting :-

# response = client.chat.completions.create(
#     model="openai/gpt-4o-mini",
#     max_tokens=300,
#     messages=[
#         {
#             "role": "user",
#             "content": """
# <INST>
# You are a mathematical solver.
# Follow START -> PLAN -> OUTPUT -> END.
# Return JSON array with fields: step, content.

# Solve 2+2*4/8
# </INST>
# """
#         }
#     ]
# )


# majorly we use chatml and inst style prompting, but we can also use alpaca style prompting, it depends on the use case and the model we are using,
#  some models are trained on specific style of prompting, so we can use that style to get better results.



