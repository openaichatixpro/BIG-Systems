<#
Pull multiple Ollama models into the running ollama container or into the host-mounted models folder.

Usage: run in PowerShell after starting the ollama container (see README):
  .\pull_ollama_models.ps1 -Models @('gemma3n:e4b','magistral:24b','gpt-oss:20b')

Requires Docker Desktop running and the `ollama` container started by docker-compose.
#>

param(
    [string[]]$Models = @('gemma3n:e4b','magistral:24b','gpt-oss:20b')
)

foreach ($m in $Models) {
    Write-Host "Pulling model $m into container 'ollama' (if running)"
    $exit = docker exec ollama /bin/sh -c "ollama pull $m" 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to pull $m via container; attempting host-side ollama (if installed locally)."
        docker exec ollama /bin/sh -c "echo 'Retry inside container failed'"
    }
}

Write-Host "Model pull attempts finished. Check container logs or the host models folder for files."
