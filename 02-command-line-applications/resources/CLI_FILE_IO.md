# Working with Files

## Open and read files

Use the `open()` method to open files from the OS, and `read()`, or `readline()` methods to start reading the contents. When are you done with a file, always remember to `close()` it.


##### animals.txt

```
Turtle
Python
Tardigrade
```

##### console

```python
>>> animals = open('animals.txt', 'r')

# Output the entire contents of the file
>>> print(animals.read())
Turtle
Python
Tardigrade

# Output one line of the file. Line are delimited by the newline character
>>> print(animals.readline())
Turtle

# Output one line at a time, with logic
>>> for animal in animals:
>>>   print("I found a {0}".format(animal))
I found a Turtle

I found a Python

I found a Tardigrade

# Done with the file. Close it.
>>> animals.close()
```

## Writing to files

To write to a file, you still use `open()` but the second argument is now `w` for write-mode. Remember to close the file after you are done with it, whether you have it open for reading or writing.

```python
>>> animals = open('animals.txt', 'w')
>>> animals.write('Red Panda')
>>> animals.close()
>>> animals = open('animals.txt', 'r')
>>> print(animals.read())
Turtle
Python
Tardigrade
Red Panda

>>> animals.close()
```
