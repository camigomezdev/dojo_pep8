@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r app.py
env\Scripts\autopep8.exe -i -r app\controllers\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\default.py
env\Scripts\autopep8.exe -i -r app\models\__init__.py
env\Scripts\autopep8.exe -i -r app\models\codebreaker.py
env\Scripts\autopep8.exe -i -r app\models\errors.py
env\Scripts\autopep8.exe -i -r app\models\validations.py
env\Scripts\autopep8.exe -i -r app\tests\__init__.py
env\Scripts\autopep8.exe -i -r app\tests\test_codebreaker.py
env\Scripts\autopep8.exe -i -r app\views\__init__.py
env\Scripts\autopep8.exe -i -r app\views\default.py
pause
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe app.py
env\Scripts\flake8.exe app\controllers\__init__.py
env\Scripts\flake8.exe app\controllers\default.py
env\Scripts\flake8.exe app\models\__init__.py
env\Scripts\flake8.exe app\models\codebreaker.py
env\Scripts\flake8.exe app\models\errors.py
env\Scripts\flake8.exe app\models\validations.py
env\Scripts\flake8.exe app\tests\__init__.py
env\Scripts\flake8.exe app\tests\test_codebreaker.py
env\Scripts\flake8.exe app\views\__init__.py
env\Scripts\flake8.exe app\views\default.py
pause
pause
ECHO -----------------------------------------
ECHO Runing PyLint...
ECHO -----------------------------------------
env\Scripts\pylint.exe app.py
env\Scripts\pylint.exe app\controllers\__init__.py
env\Scripts\pylint.exe app\controllers\default.py
env\Scripts\pylint.exe app\models\__init__.py
env\Scripts\pylint.exe app\models\codebreaker.py
env\Scripts\pylint.exe app\models\errors.py
env\Scripts\pylint.exe app\models\validations.py
env\Scripts\pylint.exe app\tests\__init__.py
env\Scripts\pylint.exe app\tests\test_codebreaker.py
env\Scripts\pylint.exe app\views\__init__.py
env\Scripts\pylint.exe app\views\default.py
pause
pause