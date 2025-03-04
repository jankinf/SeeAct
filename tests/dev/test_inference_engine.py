from seeact_package.seeact.demo_utils.inference_engine import (
    OpenaiEngine_MindAct,
    OpenAIEngine,
)
from dotenv import load_dotenv
import litellm
import os


def openai_api():
    from openai import OpenAI

    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="token-abc123",
    )

    completion = client.chat.completions.create(
        # model="llava-hf/llava-1.5-7b-hf",
        model="deepseek-ai/deepseek-vl2",
        messages=[{"role": "user", "content": "Tell me a joke"}],
    )

    print(completion.choices[0].message)


def text_engine():
    load_dotenv(
        dotenv_path="/home/fangzhengwei/projects/fork_seeact/seeact/.env_dev",
        override=True,
        verbose=True,
    )
    # litellm.set_verbose = True

    prompt = [{"role": "user", "content": "Tell me a joke!"}]
    model = modelname

    print(os.getenv("OPENAI_API_KEY"))
    print(os.getenv("OPENAI_API_BASE"))

    engine = OpenaiEngine_MindAct(model=model)

    # high level api
    output = engine.generate(
        prompt,
        max_new_tokens=256,
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        api_base=os.getenv("OPENAI_API_BASE"),
        custom_llm_provider="openai",
    )
    print(output)

    # low level api
    # response = litellm.completion(
    #     model=model,
    #     messages=prompt,
    #     max_tokens=50,
    #     temperature=0,
    #     api_key=os.getenv("OPENAI_API_KEY"),
    #     api_base=os.getenv("OPENAI_API_BASE"),
    #     custom_llm_provider="openai",
    # )


def vision_text_engine():
    load_dotenv(
        dotenv_path="/home/fangzhengwei/projects/fork_seeact/seeact/.env_dev",
        override=True,
        verbose=True,
    )
    # litellm.set_verbose = True

    prompt = [
        "You are a helpful assistant.",
        "Describe the image.",
        "",
    ]
    model = modelname

    print(os.getenv("OPENAI_API_KEY"))
    print(os.getenv("OPENAI_API_BASE"))

    engine = OpenAIEngine(model=model)

    # high level api
    output = engine.generate(
        prompt,
        max_new_tokens=256,
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        api_base=os.getenv("OPENAI_API_BASE"),
        custom_llm_provider="openai",
        image_path="for_test.png",
    )
    print(output)

    # low level api
    # response = litellm.completion(
    #     model=model,
    #     messages=prompt,
    #     max_tokens=50,
    #     temperature=0,
    #     api_key=os.getenv("OPENAI_API_KEY"),
    #     api_base=os.getenv("OPENAI_API_BASE"),
    #     custom_llm_provider="openai",
    # )


if __name__ == "__main__":
    # modelname = "gpt-4o-2024-08-06"
    # modelname = "llava-hf/llava-1.5-7b-hf"
    # modelname = "gpt-3.5-turbo"
    modelname = "deepseek-ai/deepseek-vl2"

    openai_api()
    # vision_text_engine()
