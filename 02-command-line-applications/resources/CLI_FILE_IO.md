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

Keep in mind that in write-mode, the existing contents of the file, if any, will be overwritten.

```python
>>> animals = open('animals.txt', 'w')
>>> animals.write('Red Panda')
>>> animals.close()
>>> animals = open('animals.txt', 'r')
>>> print(animals.read())

Red Panda

>>> animals.close()
```

## Appending to files

To append to the contents of a file, you still use `open()` but the second argument is now `a` for append-mode. Remember to close the file after you are done with it.

```python
>>> animals = open('animals.txt', 'a')
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

# With Statement

It is also good practice to use the `with` keyword when dealing with file objects. This has the advantage that the file is properly closed after its block logic finishes, even if an exception is raised on the way.

```python
def read_flowers(self):

with open("flowers", "r") as flowers:
  flower_set = { flower.title() for flower in flowers }

return flower_set

```
