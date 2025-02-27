from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", None),
    base_url=os.getenv("OPENAI_API_BASE", None),
)
system_prompt = "you're a helpful assistant"

prompt_input = [
    {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
    {
        "role": "user",
        "content": [{"type": "text", "text": "tell me a joke"}],
    },
]

response = client.chat.completions.create(
    # model="gpt-4o-2024-11-20",
    model="gpt-4o-2024-08-06",
    messages=prompt_input,
    max_tokens=50,
    temperature=0,
)

answer = [choice.message.content for choice in response.choices][0]
print(answer)
