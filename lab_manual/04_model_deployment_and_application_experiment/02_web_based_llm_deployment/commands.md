# Web-based LLM Deployment Commands

## Start llama.cpp Web Service

```bash
llama-server.exe -m DeepSeek-R1-Distill-Qwen-1.5B-Q6_K_L.gguf -c 2048
```

## Parameter

| Parameter | Meaning |
|---|---|
| `-m` | model path |
| `-c` | prompt context length; Lab Guide uses `2048` |

## Optional Notebook

The Lab Guide references this notebook:

```text
https://certification-data.obs.cn-north-4.myhuaweicloud.com/CHS/HCIA-AI/V4.0/chapter5/Web%20API%20InVoking.ipynb
```

## Install OpenAI Library

```bash
pip install openai
```

