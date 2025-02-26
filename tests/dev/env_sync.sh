pip install pip-tools
pip freeze > requirements.in

pip-compile requirements.in

pip-sync requirements.txt