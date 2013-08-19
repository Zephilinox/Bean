SETLOCAL ENABLEEXTENSIONS
SETLOCAL ENABLEDELAYEDEXPANSION
MODE CON: COLS=100 LINES=60

:init
@echo off

:: this is to support paths with spaces and strange characters
set CD="!CD!"
set msyspp_params=-strict -id-folder -hide-tags -hide-global-vars -hide-dialog-states -hide-scripts -list-resources -compile-data
set PATH=""

:: specify what folders are included in the search path for scripts
set PYTHONPATH=%PYTHONPATH%;!CD:~1,-1!\ID;!CD:~1,-1!\Header;!CD:~1,-1!\Process;!CD:~1,-1!\Data;!CD:~1,-1!

MS++\MS++.exe %msyspp_params%

echo.
echo Script processing has ended.
echo.

echo Copying /Output to Warband Directory...

start xcopy "Output" "Z:\Games\Mount & Blade Warband 1.157\Modules\Bean" /e /i /h /y

echo.
echo Press any key to restart. . .
pause>nul
echo.
goto :init