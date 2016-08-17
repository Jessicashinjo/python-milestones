# Zoolandia SQL

## Setup

```
mkdir -p ~/workspace/python/exercises/zoosql && cd $_
sqlite3 zoolandia.db
```

## Requirements

You are going to use the `sqlite3` Python package to perform a series of SQL operations against the `zoolandia.db` database. If you have not done so yet, you should create the [Zoolandia ERD](./DBS_ZOOLANDIA_ERD.md) for your reference in this exercise.

Instead of a menu system, you're going to use command line arguments to manage all operations. Do not worry about unit tests for this exercise, either, since the focus is on learning to use SQL resultsets in a Python module.

## Create Species

Create a method whose purpose is to insert a new species into a `Species` table. You should create the table if it doesn't exist (see [Amazon resource](../resources/DBS_PYTHON_SQLITE3.md) file for reference). Then perform an `INSERT` SQL operation to create a new row in the table based on command line arguments.

```sh
python zoo.py create species Tenodera Mantis https://en.wikipedia.org/wiki/Tenodera
```

## Create Habitat Type

Create a method whose purpose is to insert a new row into a `HabitatType` table. You should create the table if it doesn't exist. Then perform an `INSERT` SQL operation to create a new row in the table based on command line arguments.

```sh
python zoo.py create habitattype Aquatic
python zoo.py create habitattype Forest
```

## Create Habitat

Create a method whose purpose is to insert a new row into a `Habitat` table. You should create the table if it doesn't exist. Then perform an `INSERT` SQL operation to create a new row in the table based on command line arguments.

```sh
python zoo.py create habitat Freshwater Aquatic True
python zoo.py create habitat 'Rain Forest' Forest True
```

## Create Animal

Create a method whose purpose is to insert a new species into an `Animal` table. You should create the table if it doesn't exist. Then perform an `INSERT` SQL operation to create a new row in the table based on command line arguments.

```sh
python zoo.py create animal Teddy 'Rain Forest' 1 Tenodera
```

## Create Employee

Create a method whose purpose is to insert a new row into an `Employee` table. You should create the table if it doesn't exist. Then perform an `INSERT` SQL operation to create a new row in the table based on command line arguments.

```sh
python zoo.py create employee 'Hank Ross' 42
python zoo.py create employee 'Abigail Williams' 30
```

## Add Employee to Habitat

Create a method whose purpose is to insert a new row into a `HabitatEmployee` table. You should create the table if it doesn't exist. Then perform an `INSERT` SQL operation to create a new row in the table based on command line arguments.

```sh
python zoo.py assign employee 'Hank Ross' Freshwater
python zoo.py assign employee 'Abigail Williams' 'Rain Forest'
```

## Reassign Animals to Habitats

Create a method whose purpose is to execute an [UPDATE SQL command](http://www.tutorialspoint.com/sqlite/sqlite_update_query.htm) to change values in the `Animal` table.

```sh
python zoo.py assign animal Teddy 'Boreal Forest'
```

Here's some example code to accomplish this.

```py
with sqlite3.connect('example.db') as conn:
  c = conn.cursor()

  c.execute("select HabitatId from Habitat where name=?", (habitat_name))
  target_habitat = c.fetchone()

  # Since you used fetchone(), the target_habitat variable will hold a 
  # tuple with a single value in it
  c.execute("update Animal set Habitat=? where name=?", (target_habitat[0], animal_name))

  # Since you made changes to the database, remember to commit the changes
  conn.commit()

```

## Display Habitat Report

Create a method whose purpose is to produce a report showing the animals and the employees assigned to each habitat.

> **Example report:** You may choose how to display the report. It does not have to look like this.

```sh
Habitat              Animals            Employees
=========================================================
Rain Forest          Teddy              Abigail Williams
                     Wally
                     Zipper
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Freshwater           Nemo               Hank Ross
                     Dory
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```










