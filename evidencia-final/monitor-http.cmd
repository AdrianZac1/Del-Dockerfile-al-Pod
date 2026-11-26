
@echo off
:monitor
echo %date% %time%
curl.exe --max-time 3 -sS -o NUL -w "HTTP %%{http_code}\n" http://127.0.0.1:9091/healthz
timeout /t 2 /nobreak >nul
goto monitor
