@echo off
SET PATH=%PATH%;C:\Python27
python compile.py tag %1 %2 %3 %4 %5 %6 %7 %8 %9
xcopy "Z:\Programming\Python\Mount & Blade Warband\Bean\Bean" "Z:\Steam\SteamApps\common\MountBlade Warband\Modules\Bean\" /S /E /I /Q /Y
pause

