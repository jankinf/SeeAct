from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="token-abc123",
)

models = client.models.list()
model = models.data[0].id
# model = "deepseek-ai/deepseek-vl2"
print(model)

completion = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who are you?"}
  ]
)

print(completion.choices[0].message)