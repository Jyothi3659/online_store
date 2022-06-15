Online store project contains two applications
1. masterdata - To have all the masters information and basecontent which is abstruct class to use in all the modles
2. shop - which contains all the tables related to product and shop

How to setup project?

clone the project from git
command to clone - git clone -b master giturl (https://github.com/Jyothi3659/online_store.git)

create venv - python3 -m venv (venvname)
install all the packages from requirement.txt using (pip install -r path to requirement.txt)

create a database and configure in settings.py

Create superuser (python manage.py createsuperuser)

run the server (python manage.py runserver)
login in with superuser credentials (localhost:8000/admin)

create product shop and category