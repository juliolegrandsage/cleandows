# Nettoyage du disque en supprimant les fichiers temporaires

# Suppression des fichiers temporaires dans le dossier temp
Remove-Item -Path $env:TEMP\* -Force -Recurse -ErrorAction SilentlyContinue

# Suppression des fichiers temporaires dans le dossier Windows\Temp
Remove-Item -Path "$env:SystemRoot\Temp\*" -Force -Recurse -ErrorAction SilentlyContinue

# Nettoyage des fichiers du dossier Prefetch
Remove-Item -Path "$env:SystemRoot\Prefetch\*" -Force -ErrorAction SilentlyContinue

# Nettoyage du cache de Windows Update
Remove-Item -Path "$env:SystemRoot\SoftwareDistribution\Download\*" -Force -Recurse -ErrorAction SilentlyContinue

# Nettoyage du cache des composants Windows
Start-Process -FilePath Cleanmgr.exe -ArgumentList '/VeryLowDisk' -Wait

Write-Host "Nettoyage du disque terminé."
