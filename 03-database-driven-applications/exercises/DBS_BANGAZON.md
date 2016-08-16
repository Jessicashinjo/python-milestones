# Bangazon with a Database

## Setup

1. Make sure your team has a [Bangazon ERD](../DBS_BANGAZON_ERD.md) before you attempt to complete this exercise.
1. Create a SQLite database for your project. You can do this on the command line, or via the DB Browser application.
1. Use the `sqlite3` package to start interacting with your database for persisting data instead of serialized files.
1. Use `INSERT` statements to create your data and `SELECT` statements to query them back out.

## Requirements

1. You're going to replace all the code that saved the data as serialized objects in files to now use SQL and store the data in SQLite.
1. Use your ERD to help guide you how to insert data, and query/join data based on the keys and foreign keys.