@echo off

REM This script is to simply start bot.py from a bat script for the skids


REM Attenpt to start py launcher without relying on PATH
%SYSTEMROOT%\py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO attempt
%SYSTEMROOT%\py.exe -m bot
GOTO end

REM Attempts to run pythong relying on PATH
:attempt
py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO lastattempt
py.exe -m bot
PAUSE
GOTO end

REM As a last resortm attempt to run whatever python there is
:lastattempt
python.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO message
python.exe bot
PAUSE
GOTO end

:message
echo "Python was not found on your system. Please install python 3.8 and try again."
PAUSE

:end