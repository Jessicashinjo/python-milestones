# Bangazon with a Database

## Prerequisite

Make sure you have an approved [Bangazon ERD](../DBS_BANGAZON_ERD.md) before you attempt to complete this exercise.

## Setup

1. Fork your team's Bangazon project into your account.
1. `cd ~/workspace/python/exercises`
1. Clone the project into a new `bangazondb` directory. If you've never done this before, you can override git's default behavior of creating a new sub-directory based on the project name.

    > `git clone {url} {specific directory name}`


## Requirements

1. You're going to replace all the code that saved the data as serialized object in text files to now use SQL and store the data in SQLite.
1. Use your ERD to help guide you how to insert data, and query/join data based on the keys and foreign keys.