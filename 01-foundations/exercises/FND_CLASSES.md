# Classes

## Setup

```
mkdir -p ~/workspace/python/exercises/classes && cd $_
touch employees.py
```

## Instructions

Create a class that contains information about employees of a company and define methods to get employee name, job title, and start date. Print a list that contains profiles for 3 company employees.
    ```
    class Company(object):

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getTitle(self):
        return self.start_date
    }
    ```
##
