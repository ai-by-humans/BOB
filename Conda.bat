@echo off
color 0E
setlocal enabledelayedexpansion

:: Step 1
echo Conda installer made by ai-by-humans.com
pause

:: Step 2
if not exist "installers" mkdir "installers"
if not exist "env" mkdir "env"

:: Step 3
cd installers
if not exist Miniconda3-latest-Windows-x86_64.exe (
    echo Downloading Miniconda...
    powershell -Command "& { Invoke-WebRequest -Uri https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -OutFile Miniconda3-latest-Windows-x86_64.exe }"
) else (
    echo Miniconda installer already exists.
)
cd ..

:: Step 4
if not exist "env\Miniconda3" (
    echo Installing Miniconda...
    start /wait installers\Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%CD%\env\Miniconda3
) else (
    echo Miniconda is already installed.
)

:: Step 5
set /p createEnv="Do you want to create a new conda environment? (y/n): "
if /i "!createEnv!"=="y" goto :CreateEnv
goto :End

:CreateEnv
:: Step 6
set /p envName="Enter the name for the new conda environment: "
set /p pythonVersion="Enter the Python version to use (e.g., 3.8): "
env\Miniconda3\Scripts\conda create --name !envName! python=!pythonVersion! -y

:: Step 7
echo @echo off > !envName!.bat
echo call env\Miniconda3\Scripts\activate.bat !envName! >> !envName!.bat
echo cmd /k >> !envName!.bat
echo Environment '!envName!' created and batch file '!envName!.bat' generated.

:End
endlocal
pause
