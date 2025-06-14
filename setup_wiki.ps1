# setup_wiki.ps1
# Script de instalación, limpieza y ejecución local para wiki_documental

# --- CONFIGURACIÓN INICIAL ---
$projectPath = "C:\WorkFolder\wiki_documental_audit"
$venvName = "wiki-documental"
$docPath = "inputs/originals"
$port = 5500

Write-Host "📁 Proyecto: $projectPath"
Set-Location $projectPath

# --- 1. ELIMINAR ENTORNO VIRTUAL CORRUPTO SI EXISTE ---
$envRoot = "$env:LOCALAPPDATA\pypoetry\Cache\virtualenvs"
$envMatch = Get-ChildItem -Path $envRoot -Directory | Where-Object { $_.Name -like "$venvName*" }

if ($envMatch) {
    Write-Host "🧹 Eliminando entorno virtual corrupto..."
    foreach ($match in $envMatch) {
        Remove-Item -Recurse -Force "$($match.FullName)"
    }
}

# --- 2. POETRY INSTALL ---
Write-Host "📦 Instalando dependencias con Poetry..."
poetry env remove python 2>$null
poetry install

if ($LASTEXITCODE -ne 0) {
    Write-Error "❌ Error durante poetry install. Abortando."
    exit 1
}

# --- 3. ACTIVAR ENTORNO ---
$venvPath = poetry env info --path
Write-Host "✅ Entorno activado: $venvPath"
& "$venvPath\Scripts\Activate.ps1"

# --- 4. LIMPIEZA OPCIONAL ---
Write-Host "🧼 Ejecutando limpieza previa (wiki reset)..."
poetry run wiki reset

# --- 5. INGESTA DE DOCUMENTOS ---
$docFiles = Get-ChildItem "$projectPath\$docPath" -Filter *.docx
if ($docFiles.Count -eq 0) {
    Write-Warning "⚠️ No se encontraron archivos DOCX en $docPath"
} else {
    foreach ($doc in $docFiles) {
        Write-Host "📥 Ingestando: $($doc.Name)"
        poetry run wiki ingest "$($doc.FullName)"
    }
}

# --- 6. LANZAR SERVIDOR WEB LOCAL ---
Write-Host "🌐 Iniciando servidor web en http://localhost:$port..."
Start-Process "http://localhost:$port"

# Construir el comando como string completo entre comillas dobles
$cmd = "python -m http.server $port -d wiki"
Start-Process powershell.exe -ArgumentList "-NoExit", "-Command `"$cmd`""
