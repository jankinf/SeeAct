
export HF_HUB_OFFLINE=1
export LD_LIBRARY_PATH=/home/fangzhengwei/miniconda3/envs/seeact/lib/python3.10/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH
# CUDA_VISIBLE_DEVICES=0 vllm serve deepseek-ai/Janus-Pro-7B --dtype auto --api-key token-abc123 --trust-remote-code


# CUDA_VISIBLE_DEVICES=0 vllm serve llava-hf/llava-1.5-7b-hf --dtype auto --api-key token-abc123 --trust-remote-code

# CUDA_VISIBLE_DEVICES=0 python test_llava.py --num-prompts 1
# CUDA_VISIBLE_DEVICES=0 python test_vllm.py


# curl -X POST "http://localhost:8000/v1/completions" \
#   -H "Content-Type: application/json" \
#   -H "Authorization: token-abc123" \
#   -d '{
#     "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
#     "name": "Math Tutor",
#     "tools": [{"type": "code_interpreter"}],
#     "model": "llava-hf/llava-1.5-7b-hf"
#   }'

# OPENAI_API_KEY = "token-abc123",
# OPENAI_API_BASE = "http://localhost:8000/v1",

python openai_api.py