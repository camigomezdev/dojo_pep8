@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing PyLint...
ECHO -----------------------------------------
env\Scripts\pylint.exe app.py
env\Scripts\pylint.exe app\__init__.py
env\Scripts\pylint.exe app\controllers\__init__.py
env\Scripts\pylint.exe app\controllers\default.py
env\Scripts\pylint.exe app\decorators\__init__.py
env\Scripts\pylint.exe app\decorators\decorators_views.py
env\Scripts\pylint.exe app\models\__init__.py
env\Scripts\pylint.exe app\models\codebreaker.py
env\Scripts\pylint.exe app\models\errors.py
env\Scripts\pylint.exe app\models\validations.py
env\Scripts\pylint.exe app\tests\__init__.py
env\Scripts\pylint.exe app\tests\test_codebreaker.py
env\Scripts\pylint.exe app\views\__init__.py
env\Scripts\pylint.exe app\views\default.py
pause