Ollama model pull guide

You have two options to ensure `gemma3n:e4b` is available in the `ollama_models` volume.

Option A — use the `ollama-init` service (recommended for automation):

1. Start the ollama service (it will create the volume):
   docker-compose up -d ollama

2. Run the init job which mounts the same volume and pulls the model:
   docker-compose run --rm ollama-init

This runs once and exits. The model will remain persisted in the `ollama_models` named volume.

Option B — manual pull inside the running container:

1. Start ollama:
   docker-compose up -d ollama

2. Exec into the container and pull the model:
   docker exec -it ollama /bin/sh -c "ollama pull gemma3n:e4b"

Notes:
- Pulling can take a long time and requires internet access.
- If you hit permission errors, ensure the volume is writable by the container user.
- After the model is present you can run: ollama run gemma3n:e4b
- If you need the model on host storage instead of the named volume, mount a host folder to `/root/.ollama` in the `ollama` service.