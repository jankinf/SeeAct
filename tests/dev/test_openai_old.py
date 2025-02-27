from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = "you're a helpful assistant"

prompt_input = [
    {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "tell me a joke"}
        ],
    },
]

response = openai.ChatCompletion.create(
    model="gpt-4o-2024-11-20",
    messages=prompt_input,
    max_tokens=50,
    temperature=0,
)
answer = [choice["message"]["content"] for choice in response["choices"]][0]
print(answer)
