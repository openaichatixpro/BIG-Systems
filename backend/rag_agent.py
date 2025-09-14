"""
Simple RAG agent example (placeholder).

This file shows a minimal retrieval + prompt composition flow that can be extended.
It does not require heavy ML libraries and uses local file scanning for 'documents'.
"""
import os
import json
from typing import List


def load_documents(doc_dir: str) -> List[str]:
    docs = []
    if not os.path.isdir(doc_dir):
        return docs
    for fn in os.listdir(doc_dir):
        path = os.path.join(doc_dir, fn)
        if os.path.isfile(path) and fn.lower().endswith('.txt'):
            with open(path, 'r', encoding='utf-8') as f:
                docs.append(f.read())
    return docs


def simple_retrieve(query: str, docs: List[str], top_k: int = 3) -> List[str]:
    # naive retrieval based on substring match and length
    scored = []
    for d in docs:
        score = 0
        if query.lower() in d.lower():
            score += 10
        score += max(0, 5 - abs(len(d.split()) - len(query.split())))
        scored.append((score, d))
    scored.sort(reverse=True)
    return [d for s, d in scored[:top_k]]


def compose_prompt(query: str, contexts: List[str]) -> str:
    prompt = """
You are a helpful assistant. Use the following context passages to answer the user's question.

Context:
"""
    for i, c in enumerate(contexts, start=1):
        prompt += f"\n[{i}] {c[:500]}\n"
    prompt += f"\nQuestion: {query}\nAnswer:" 
    return prompt


def run_example():
    docs = load_documents('/data')
    q = 'What is the status file?' 
    contexts = simple_retrieve(q, docs)
    prompt = compose_prompt(q, contexts)
    print('Prompt:\n', prompt)


if __name__ == '__main__':
    run_example()
