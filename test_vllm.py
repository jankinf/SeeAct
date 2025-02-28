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
