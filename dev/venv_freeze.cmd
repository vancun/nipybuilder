call %~dp0\venv_activate.cmd
pip freeze > %~dp0\..\requirements.txt
