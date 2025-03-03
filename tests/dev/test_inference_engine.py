from seeact_package.seeact.demo_utils.inference_engine import OpenaiEngine_MindAct
from dotenv import load_dotenv
import litellm
import os


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

load_dotenv()
litellm.set_verbose = True

prompt = [{"role": "user", "content": "Hello world"}]
# model = "gpt-4o-2024-08-06"
model = "llava-hf/llava-1.5-7b-hf"
# model = "gpt-3.5-turbo"

engine = OpenaiEngine_MindAct(model=model)
# high level api
output = engine.generate(
    prompt,
    max_new_tokens=50,
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
    api_base=os.getenv("OPENAI_API_BASE"),
    # custom_llm_provider="custom_openai",
    custom_llm_provider="openai",
)

# low level api
# response = litellm.completion(
#     model=model,
#     messages=prompt,
#     max_tokens=50,
#     temperature=0,
#     api_key=os.getenv("OPENAI_API_KEY"),
#     api_base=os.getenv("OPENAI_API_BASE"),
#     custom_llm_provider="custom_openai",
# )
