@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe main.py
env\Scripts\flake8.exe codebreaker.py
env\Scripts\flake8.exe test\test_codebreaker.py
pause