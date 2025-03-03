from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
from PIL import Image
import requests

# load the processor
processor = AutoProcessor.from_pretrained(
    'allenai/Molmo-7B-D-0924',
    trust_remote_code=True,
    torch_dtype='auto',
    device_map='auto'
)

import pdb; pdb.set_trace()
inputs = processor.process(
    images=[Image.open(requests.get("https://picsum.photos/id/237/536/354", stream=True).raw)],
    text="Describe this image."
)

import pdb; pdb.set_trace()
modelnames = [
    "rhymes-ai/Aria",
    "deepseek-ai/deepseek-vl2-tiny",
    "deepseek-ai/deepseek-vl2",
    "THUDM/glm-4v-9b",
    "h2oai/h2ovl-mississippi-800m",
    "HuggingFaceM4/Idefics3-8B-Llama3",
    "OpenGVLab/InternVL2-2B",
    "HwwwH/MiniCPM-V-2",
    "openbmb/MiniCPM-Llama3-V-2_5",
    "openbmb/MiniCPM-V-2_6",
    "openbmb/MiniCPM-o-2_6",
    "meta-llama/Llama-3.2-11B-Vision-Instruct",
    "allenai/Molmo-7B-D-0924",
    "nvidia/NVLM-D-72B",
    "mistral-community/pixtral-12b",
    "Qwen/Qwen2-VL-7B-Instruct",
    "Qwen/Qwen2.5-VL-3B-Instruct",
]



for modelname in modelnames:
    try:
        tokenizer = AutoTokenizer.from_pretrained(modelname, trust_remote_code=True)
        messages = [
            {"role": "assistant", "content": "You are a helpful assistant"},
            {"role": "user", "content": "tell me a joke"},
        ]
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
    except Exception as e:
        print(f"{modelname}".center(20, '*'))
        print(f"{e}")
        print("".center(20, '*') + '\n\n')
        continue


import pdb

pdb.set_trace()
from seeact_package.seeact.demo_utils.vllm_vl_helper import (
    model_example_map,
    SamplingParams,
    LLM,
)
from PIL import Image
from torch import distributed as dist

modality = "image"
llm, prompt, stop_token_ids = model_example_map["deepseek_vl_v2"](modality)
llm: LLM
image_data = Image.open("for_test.png").convert("RGB")
input_prompt = prompt.format(question="Describe this image")

sampling_params = SamplingParams(
    temperature=0.2, max_tokens=64, stop_token_ids=stop_token_ids
)
inputs = {
    "prompt": input_prompt,
    "multi_modal_data": {modality: image_data},
}

# llm.llm_engine.tokenizer.tokenizer.apply_chat_template(
#     [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": prompt},
#     ],
#     tokenize=False,
#     add_generation_template=True,
# )


outputs = llm.generate(inputs, sampling_params=sampling_params)
responses = [output.outputs[0].text for output in outputs]
print(responses)

if dist.is_initialized():
    dist.destroy_process_group()
