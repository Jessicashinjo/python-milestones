#Let's Learn Some Django

## Setup

```
mkdir -p ~/workspace/python/exercises/djangotime && cd $_
```

## Instructions


Create virtual environment

```
$ python3 -m venv myvenv
(replace myenv with name of your virtual environment)
```

Switch to
```
$ workon myvenv
```

```
$ pip install django
```

```
$ django-admin startproject myblogs .
```

```
python manage.py migrate
```

```
python manage.py runserver
```
