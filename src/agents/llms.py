# # implemening a custom tokenizer in python 

# import tiktoken

# enc = tiktoken.encoding_for_model("gpt-4o")
# text = "Hello, how are you doing today?"
# tokens = enc.encode(text)


# # [13225, 11, 1495, 553, 481, 5306, 4044, 30]
# print(tokens)

# decoded = enc.decode([13225, 11, 1495, 553, 481, 5306, 4044, 30])
# print(decoded)


import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
x = "You are a mathematical solver. if some query not related to math, then reply with 'I can only solve mathematical problems.' "
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    max_tokens=256,
    messages=[
        {"role": "system", "content": x},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)



# zero shot prompting :- directly giving inst to the model
