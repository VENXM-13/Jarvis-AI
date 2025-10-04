from openai import OpenAI

# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
api_key="Add OpenAI Api Key ",)

completion = client.chat.completions.create(
model="gpt-4.1",
messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. I need short and concise Answers "},
    {"role": "user", "content": "What is Hyperrealism"}
]
)

print(completion.choices[0].message.content)


