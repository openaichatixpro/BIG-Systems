"""
Lightweight example of calling an Ollama model via HTTP API (no heavy ML libs).

This script shows how a simple RAG agent could call Ollama for generation.
"""
import os
import requests

OLLAMA_HOST = os.environ.get('OLLAMA_HOST', 'http://localhost:11434')


def call_model(model: str, prompt: str):
    url = f"{OLLAMA_HOST}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 256
    }
    resp = requests.post(url, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def main():
    model = 'gemma3n:e4b'
    prompt = 'Say hello and list the available endpoints in the container.'
    print('Calling model', model)
    print(call_model(model, prompt))


if __name__ == '__main__':
    main()
