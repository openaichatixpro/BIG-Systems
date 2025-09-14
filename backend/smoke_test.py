"""Quick smoke test to import backend modules and run basic functions."""
import importlib

modules = [
    'processor',
    'rag_agent',
]

for m in modules:
    print(f'Importing {m}...')
    importlib.import_module(m)
    print(f'{m} OK')

print('Smoke test completed')
