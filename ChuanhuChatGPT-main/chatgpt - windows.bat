@echo off
echo Opening ChuanhuChatGPT...

REM Open powershell via bat
start powershell.exe -NoExit -Command "python ./ChuanhuChatbot.py"

REM The web page can be accessed with delayed start http://127.0.0.1:7860/
ping -n 5 127.0.0.1>nul

REM access chargpt via your default browser
start "" "http://127.0.0.1:7860/"


echo Finished opening ChuanhuChatGPT (http://127.0.0.1:7860/).