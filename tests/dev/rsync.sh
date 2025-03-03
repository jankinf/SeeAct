# rsync -avcn --progress a100_jw:/home/chenjiawei/projects/seeact/* ./ --exclude={'__pycache__/',}
# rsync -av --progress a100_jw:/home/chenjiawei/projects/seeact/* ./ --exclude={'__pycache__/',}

# rsync -av --progress ln01:/data/zhangyichi/cache/huggingface/hub/models--llava-hf--llava-1.5-7b-hf $HF_HOME/hub/
# rsync -av --progress ln01:/data/zhangyichi/cache/huggingface/hub/models--meta-llama--Llama-3.2-11B-Vision-Instruct $HF_HOME/hub/
# rsync -av --progress ln01:/data/zhangyichi/cache/huggingface/hub/models--llava-hf--llama3-llava-next-8b-hf $HF_HOME/hub/
# rsync -av --progress ln01:/data/zhangyichi/cache/huggingface/hub/models--microsoft--Phi-3.5-vision-instruct $HF_HOME/hub/
# rsync -av --progress ln01:/data/zhangyichi/cache/huggingface/hub/models--Qwen--Qwen2-VL-7B-Instruct $HF_HOME/hub/
# rsync -av --progress ln01:/data/zhangyichi/cache/huggingface/hub/models--THUDM--glm-4v-9b $HF_HOME/hub/
# rsync -av --progress ln01:/data/zhangyichi/cache/huggingface/hub/models--OpenGVLab--InternVL2-8B $HF_HOME/hub/
rsync -av --progress ln01:/data/zhangyichi/cache/huggingface/hub/models--deepseek-ai--deepseek-vl2 $HF_HOME/hub/