# Bash Builder

This exercise will assist in your understanding of [using bash scripts for automation](https://github.com/nashville-software-school/python-milestones/blob/master/02-command-line-applications/resources/CLI_BASH_SCRIPTING.md)

## Setup

```
mkdir -p ~/workspace/python/exercises/cli && cd $_
touch grocery.txt clothing.txt jewelry.txt reader.py writer.py builder.sh
chmod +x builder.sh
```

## Instructions

You've been making lists of things you want to purchase, but, due to the thoughts randomly popping into your head, you've just thrown the purchaes into a text file all willy-nilly.  Now that you're looking to go shopping, you'd like to have a more organized list to take with you, but who has the time to organize lists by hand?  Create a program flow that works as follows.

1. A Python module that:
  1. Takes an argument specifying a text file to read.
  ```bash
  python reader.py grocery
  ```
  2. Reads each line of that text file.
  3. Outputs a space-delimited string of items.
2. A Python module that:
  1. Takes a number of arguments.
  ```bash
  python writer.py orange banana kumquat lemon
  ```
  2. Organizes those arguments' values alphabetically.
  3. Writes the values prefixed by their order in the list to a new text file. (i.e.`1. apple`)
3. A bash script that:
  1. Takes a single argument as input.
  ```bash
  ./builder.sh grocery
  ```
  2. Passes that argument to the first Python module.
  3. Recieves the output from the first Python module and passes it to the second Python module.

## Requirements

**Write tests for Python functionality before writing implementation code**

* Populate `grocery.txt` with grocery items, one per line.
* Populate `clothing.txt` with cloting items, one per line.
* Populate `jewelry.txt` with jewelry items, one per line.
* Output the final list to `currentitems.txt`.

## Bonus features

* Ensure the program can handle items with spaces.
* Allow the program to be run multiple times, sequentially, adding each list to `currentitems.txt` with an appropriate heading.
