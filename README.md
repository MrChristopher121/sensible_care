# Quick start


> 👉 Create new folder

```shell
$ cd code
$ mkdir sensible_care
$ cd sensible_care
```


> 👉 Install modules via virtual environment  

```shell
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
(.venv) $ pip install django
(.venv) $ pip install black # enforces code formatting
(.venv) $ pip install psycopg2-binary # to connect to postgres
(.venv) $ pip install python-dotenv   # to load environment variables
# Remember to create .env file and update django_project/settings.py
# Remember to channge database to postgres in django_project/settings.py
```


> 👉 Start django project

```shell
(.venv) $ django-admin startproject django_project .
(.venv) $ python manage.py startapp dashboard
# Remember to add "dashboard" to django_project/settings.py INSTALLED_APPS
```


> 👉 Set Up Database

```shell
(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
```


> 👉 Create the Superuser

``` shell
(.venv) $ python manage.py createsuperuser
```


> 👉 Freeze requirements

```shell
(.venv) $ pip freeze > requirements.txt
```


> 👉 Set Up Git

```shell
(.venv) $ git init
(.venv) $ git remote add origin https://github.com/amonteagle/sensible_care.git
(.venv) $ git branch -M main
(.venv) $ git status
(.venv) $ git add -A
(.venv) $ git commit -m "Initial commit"
(.venv) $ ggit push -u origin main

```


> 👉 Start the app

```shell
(.venv) $ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`



