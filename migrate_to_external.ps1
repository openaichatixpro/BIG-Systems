<#
Safe migration helper (PowerShell) - non-destructive copy of this project to external host path.

Usage (PowerShell):
  .\migrate_to_external.ps1 -DestinationPath 'I:\Facebook_RF-BG\Facebook_RF\Facebook_RF\New folder' -DryRun

This will copy files while preserving timestamps and will skip large folders if you choose.
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$DestinationPath,
    [switch]$DryRun
)

Write-Host "Preparing to copy project to: $DestinationPath"

if (-not (Test-Path -Path $DestinationPath)) {
    Write-Host "Creating destination: $DestinationPath"
    if (-not $DryRun) { New-Item -ItemType Directory -Path $DestinationPath -Force | Out-Null }
}

$source = (Get-Location).Path
Write-Host "Source: $source"

# Exclude large model folders and node_modules by default
$excludes = @('**/node_modules','**/.git','**/ollama_models','**/I:/ollama_models')

Write-Host "Excluding: $($excludes -join ', ')"

if ($DryRun) {
    Write-Host "Dry run: listing files that would be copied..."
    robocopy $source $DestinationPath /L /E /NJH /NJS /NP /XF $excludes | Out-Host
    Write-Host "Dry run complete. Rerun without -DryRun to perform copy."
    exit 0
}

Write-Host "Starting copy (this may take time)."
# Use robocopy for reliable copying on Windows
robocopy $source $DestinationPath /E /COPY:DAT /R:3 /W:5 /NFL /NDL /NJH /NJS /NP | Out-Host

Write-Host "Copy finished. You may now start docker-compose with -f docker-compose.yml -f docker-compose.host.yml"
