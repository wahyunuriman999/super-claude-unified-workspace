# Installation script for AEGIS v5.1 on Windows

$targetDir = "$env:USERPROFILE\.gemini\config\skills\aegis"

Write-Host "Installing AEGIS v5.1 global skill on Windows..."
if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
}

Copy-Item -Recurse -Force -Path "aegis\*" -Destination $targetDir

Write-Host "Successfully installed AEGIS v5.1 to $targetDir" -ForegroundColor Green
Write-Host "Restart your AI agent or IDE to reload the custom skills."
