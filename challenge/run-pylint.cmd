@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing PyLint...
ECHO -----------------------------------------
env\Scripts\pylint.exe main.py
env\Scripts\pylint.exe codebreaker.py
env\Scripts\pylint.exe test\test_codebreaker.py
pause