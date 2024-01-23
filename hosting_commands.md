CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.api_server --model /data/akshat/lexi-models/Llama-2-7b-chat-hf --dtype=float32 --tensor-parallel-size 4
