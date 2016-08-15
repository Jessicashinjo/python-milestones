#Let's Learn Some Django

## Setup

```
mkdir -p ~/workspace/python/exercises/djangotime && cd $_
```

## Instructions


Start by creating a virtual environment

```
$ python3 -m venv myvenv
(replace myenv with name of your virtual environment. The above command will create a directory.)
```

Start working on that virtual environment.

```
$ workon myvenv
You will know you are successfully using the virtual environment when you see (myvenv).
```

Install Django

```
$ pip install django
```

Create the files for this django project.
For Mac:

```
$ django-admin startproject myblogs .
```

For Windows:

```
$ django-admin.py startproject mysite .
```

Create database for the project. Make sure you run the following command in the directory where manage.py file is:

```
python manage.py migrate
```

And now we can start the web server

```
python manage.py runserver
```

Create the application (from the directory where manage.py is stored):

```
python manage.py startapp blog
```

After creating an application we also need to tell Django that it should use it. In mysite/settings/py, add a line containing 'blog' in the INSTALLED_APPS list.



Create blog post model in blog/models.py:

```
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

Create tables for models in the database:

```
$ python manage.py makemigrations blog
```
