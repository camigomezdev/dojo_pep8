@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r main.py
env\Scripts\autopep8.exe -i -r codebreaker.py
env\Scripts\autopep8.exe -i -r test\test_codebreaker.py
pause