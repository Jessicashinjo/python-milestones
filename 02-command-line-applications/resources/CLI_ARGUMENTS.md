# Command Line Arguments

When you run a Python module via the command line...

```sh
python printname.py
```

You can pass in arguments to the module to change it's behavior when it is executed. For example, let's look at a simple example of a module that simply prints out a person's name. It accepts two arguments.

1. First name
2. Last name

First, you need to import the `sys` module to access the arguments

```python
import sys
```

Then, in the mythical `__main__` method, you can use the `sys.argv` list to read the arguments. The first item in the list is going to be the name of the module itself, so you want to start reading from the second argument.

```python
if __name__ == "__main__":
  print("First name is {0}".format(sys.argv[1]))
  print("Last name is {0}".format(sys.argv[2]))
```

Then you execute the module from the CLI.

```sh
python printname.py Kylie Abromowitz
```
