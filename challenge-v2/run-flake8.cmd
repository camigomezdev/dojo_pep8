@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe app.py
env\Scripts\flake8.exe app\__init__.py
env\Scripts\flake8.exe app\controllers\__init__.py
env\Scripts\flake8.exe app\controllers\default.py
env\Scripts\flake8.exe app\decorators\__init__.py
env\Scripts\flake8.exe app\decorators\decorators_views.py
env\Scripts\flake8.exe app\models\__init__.py
env\Scripts\flake8.exe app\models\codebreaker.py
env\Scripts\flake8.exe app\models\errors.py
env\Scripts\flake8.exe app\models\validations.py
env\Scripts\flake8.exe app\tests\__init__.py
env\Scripts\flake8.exe app\tests\test_codebreaker.py
env\Scripts\flake8.exe app\views\__init__.py
env\Scripts\flake8.exe app\views\default.py
pause