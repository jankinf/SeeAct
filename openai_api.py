# from openai import OpenAI
# client = OpenAI(
#     base_url="http://localhost:8000/v1",
#     api_key="token-abc123",
# )

# completion = client.chat.completions.create(
#   model="llava-hf/llava-1.5-7b-hf",
#   messages=[
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message)


from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "token-abc123"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id

print(models)
print(model)

# Completion API
stream = False
# completion = client.completions.create(
#     model=model,
#     prompt="A robot may not injure a human being",
#     # echo=False,
#     # n=2,
#     # stream=stream,
#     # logprobs=3
# )
# completion = client.chat.completions.create(
#     model=model,
#     # prompt="A robot may not injure a human being",
#     messages=[
#         {'input': 'A robot may not injure a human being'}
#     ]
#     # [
#     #     {"role": "user", "content": "Hello!"}
#     # ]
# )

messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(model=model, messages=messages)

# print("Completion results:")
# if stream:
#     for c in completion:
#         print(c)
# else:
#     print(completion)