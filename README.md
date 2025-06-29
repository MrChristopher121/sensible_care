<<<<<<< HEAD
# Quick start


> 👉 Create new folder

```shell
$ cd code
$ mkdir sensible_care_dash
$ cd sensible_care_dash
```


> 👉 Install modules via virtual environment  

```shell
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
(.venv) $ pip install -r requirements.txt
```


> 👉 Set Up Git

```shell
(.venv) $ git init
(.venv) $ git remote add origin https://github.com/MrChristopher121/sensible_care.git
(.venv) $ git branch -M main

(.venv) $ git pull --rebase origin main
(.venv) $ git status
(.venv) $ git add -A
(.venv) $ git commit -m "Update messsage"
(.venv) $ git push -u origin main
```


> 👉 Start the app

```shell
(.venv) $ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`

