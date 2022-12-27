Help
- The semantic style sheet takes care of our styles
- To copy from windows into ubuntu copy in windows and then right click in the ubuntu terminal. That will paste what is coppied

Ubuntu
- sudo apt-get update
- sudo apt-get install python3.10 python3-pip

Flask
- Create virtual env: python3 -m venv venv
- . venv/bin/activate
- pip install Flask Flask-SQLAlchemy
- Flask-SQLAlchemy didn't work so I did: python3 -m pip install Flask-SQLAlchemy
- Make sure that "venv" is running. (you should see "(venv)")
- export FLASK_APP=app.py
- export FLASK_DEBUG=true
- flask run

FastApi
- Create virtual env: python3 -m venv venv
- . venv/bin/activate
- pip install fastapi
- Need asgi server: pip install "uvicorn[standard]"
- Template files and db support: pip install python-multipart sqlalchemy jinja2
- Make sure that "venv" is running. (you should see "(venv)")
- uvicorn app:app --reload

Django
- Follow Django tutorial 
  - https://docs.djangoproject.com/en/4.1/intro/tutorial01/
  - https://docs.djangoproject.com/en/4.1/intro/tutorial02/
  - This was important 
    - python3 manage.py makemigrations djangoApp, then migrate
  - If I want to look at the sql migration
    - use the number in this that makemigrations creates for the next command djangoApp/migrations/0001_initial.py
    - python3 manage.py sqlmigrate djangoApp 0001
- pip install Django
- sudo apt install python3-django
- django-admin startproject (projectName)
- cd (projectName)
- python manage.py startapp (appName) (auto generates the app)
- python3 manage.py makemigrations (appName)
- python3 manage.py migrate
- python3 manage.py runserver
- python3 manage.py createsuperuser