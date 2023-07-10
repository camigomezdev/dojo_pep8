@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r app.py
env\Scripts\autopep8.exe -i -r app\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\default.py
env\Scripts\autopep8.exe -i -r app\decorators\__init__.py
env\Scripts\autopep8.exe -i -r app\decorators\decorators_views.py
env\Scripts\autopep8.exe -i -r app\models\__init__.py
env\Scripts\autopep8.exe -i -r app\models\codebreaker.py
env\Scripts\autopep8.exe -i -r app\models\errors.py
env\Scripts\autopep8.exe -i -r app\models\validations.py
env\Scripts\autopep8.exe -i -r app\tests\__init__.py
env\Scripts\autopep8.exe -i -r app\tests\test_codebreaker.py
env\Scripts\autopep8.exe -i -r app\views\__init__.py
env\Scripts\autopep8.exe -i -r app\views\default.py
pause