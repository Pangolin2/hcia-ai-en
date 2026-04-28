# CLI-based LLM Deployment Commands

## Ubuntu: Download llama.cpp Executable Package

```bash
wget https://certification-data.obs.cn-north-4.myhuaweicloud.com/CHS/HCIA-AI/V4.0/chapter5/llama_cpp_ubuntu.zip
unzip llama_cpp_ubuntu.zip
cd build/bin
ll
```

## Ubuntu: Download Model File

```bash
wget https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q6_K_L.gguf
```

## Windows: Download Files

llama.cpp executable package:

```text
https://certification-data.obs.cn-north-4.myhuaweicloud.com/CHS/HCIA-AI/V4.0/chapter5/llama_cpp.zip
```

Model file:

```text
https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q6_K_L.gguf
```

## CLI Inference

```bash
llama-cli.exe -m DeepSeek-R1-Distill-Qwen-1.5B-Q6_K_L.gguf --temp 0.6
```

Colored output example:

```bash
llama-cli.exe --color -m DeepSeek-R1-Distill-Qwen-1.5B-Q6_K_L.gguf
```

## Parameters

| Parameter | Meaning |
|---|---|
| `-m` | model path |
| `-cnv` | conversation mode |
| `--chat-template` | chat template |
| `--color` | distinguish user input and model output by color |
| `--temp` | randomness of generated text; Lab Guide recommends `0.6` |
| `--repeat-penalty` | controls repeated token sequences |
| `--top-k` | selects from top-k candidates |

