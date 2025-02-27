from seeact_package.seeact.demo_utils.inference_engine import OpenaiEngine_MindAct
from dotenv import load_dotenv
import litellm
import os

load_dotenv()
litellm.set_verbose = True

prompt = [{"role": "user", "content": "Hello world"}]
model = "gpt-4o-2024-08-06"
# model = "gpt-3.5-turbo"

engine = OpenaiEngine_MindAct(model=model)
# high level api
output = engine.generate(
    prompt,
    max_new_tokens=50,
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
    api_base=os.getenv("OPENAI_API_BASE"),
    custom_llm_provider="custom_openai",
)

# low level api
response = litellm.completion(
    model=model,
    messages=prompt,
    max_tokens=50,
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
    api_base=os.getenv("OPENAI_API_BASE"),
    custom_llm_provider="custom_openai",
)
