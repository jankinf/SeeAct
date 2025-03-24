export HF_HUB_OFFLINE=1
export LD_LIBRARY_PATH=/home/fangzhengwei/miniconda3/envs/seeact/lib/python3.10/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH

PYTHONASYNCIODEBUG=1 python src/seeact.py
