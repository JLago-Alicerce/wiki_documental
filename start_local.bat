@echo off
REM Lanza servidor en 127.0.0.1:5500 apuntando a carpeta wiki\
python -m http.server 5500 -d wiki
start "" http://127.0.0.1:5500/index.html
