:: @> hi there! I'm pretty honored to see you here,
::    please feel free to copy anything. -Greetings from Swyter
::   -------------------------------------------------------------

SETLOCAL ENABLEEXTENSIONS
SETLOCAL ENABLEDELAYEDEXPANSION
MODE CON: COLS=40 LINES=40

:init
@echo off
cls && color 71 && title [ ] swysdk -- building
cd ..

:: this is to support paths with spaces and strange characters
set CD="!CD!"

:: setup our python and specify what folders are included in the search path for scripts
set PATH=!CD:~1,-1!\Builder\Python
set PYTHONPATH=%PYTHONPATH%;!CD:~1,-1!\Process;!CD:~1,-1!\Data;!CD:~1,-1!

:: the -B param overides the pyc/pyo bytecode generation, so there's no need for deleting them later :)
python -B Data\module_flora_kinds.py
python -B Data\module_ground_specs.py
python -B Data\module_skyboxes.py

title [X] swysdk -- finished
echo ______________________________
echo Script processing has ended.
echo Press any key to restart. . .
pause>nul
cd Data
goto :init