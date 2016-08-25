# Angular Angler

## Prerequisite

Except for the most foolhardy of students, you should wait until we discuss how to configure a Django application to serve an Angular application and set up routes to respond with JSON views.

## Setup

```
mkdir -p ~/workspace/python/exercises/angler && cd $_
django-admin startproject angler .
python manage.py startapp competition
```

## Instructions

Your task is to build a single page application, using Angular, that will be served by Django. This application's purpose is for fisherman to track what fish they catch, and where they caught them.

1. Design your models.
1. Define the models for your application and their properties.
1. Make a migration and run it to create the required tables.

### Views

#### Create Fisherman

Provide a form where a fisherman can create their account.

#### Login

After an account has been created, provide a login form.

#### List Catches

Once a fisherman logs in show them a list of fish that have been caught already. This list should display the type of fish and the location where it was caught. At the top of the page, provide a button to allow the creation of a new catch.

#### Add Catch

Provide a basic form that allows a fisherman to add a new catch.

1. Type of fish
1. Location of catch
