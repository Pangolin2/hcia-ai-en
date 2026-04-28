# 02 Web-based LLM Deployment

## Scope

This directory organizes code from the `Web-based LLM Deployment` experiment. It starts from a local `llama-server` service and then calls:

```text
service health endpoint
requests-based completion endpoint
OpenAI-compatible chat completion endpoint
OpenAI Python client
```

## Files

```text
commands.md
01_health_check.py
02_requests_completion.py
03_openai_compatible_requests.py
04_openai_client_call.py
```

## Prerequisite

Start the local service first:

```bash
llama-server.exe -m DeepSeek-R1-Distill-Qwen-1.5B-Q6_K_L.gguf -c 2048
```

Default service URL:

```text
http://localhost:8080
```
