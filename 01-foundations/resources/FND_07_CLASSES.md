# Python Classes

A class in Python is much like the new instances of functions that you created in JavaScript when you learned about prototypal inheritance.

Instead of using the `new` keyword, or using the newer `Object.create()` function, you simply define a class and call it like you were calling a function. Below is a perfectly valid class (that does absolutely nothing) and then gets created and invoked afterwards.

```python
# Define a class
class noop:
    pass  # Pass means "Move along, please. Nothing to see here."

# Create an instance of the class and invoke it
noop()
```

What exactly gets invoked in this case since the class has no actual logic in it. For any class, when you invoke it, it executes the `__init__` method. Since our simplistic example above didn't define any logic for the built-in `__init__` method, nothing happened.

## Simple Class

Let's define a class that actually does something when it's initialized.

```python
class Zoo:
    def __init__(self, name):
        self.zoo_name = name

a_zoo = Zoo("Zoolandia")
a_zoo.zoo_name
```

You can see that the syntax is very close to creating a new instance of a JavaScript class. Be aware that the `__init__` function may **look** like the constructor function, but it's not. It only gets invoked after the instance of the class has been fully created, and that new instance gets passed into the `__init__` function.

In fact, the class instance is the first argument to **_any_** function defined in a class.

```python
class Zoo:
    '''Zoo class contains all methods require to populate and maintain a zoo of animals
    '''

    def __init__(self, name):
        self.zoo_name = name  # Define an instance variable with self
        self.animals = dict()

    def add_animal(self, type, name):
        '''Add an animal to the zoo

        Method arguments:
        type(string) -- The type of animal to add
        name(string) -- The given name of the animal
        '''
        self.animals[name] = type

    def list_animals(self):
        '''Lists all animals in the zoo

        Method arguments:
        n/a
        '''
        [print(k + ' the ' + v) for k, v in self.animals.items()]

a_zoo = Zoo("Zoolandia")
a_zoo.add_animal("Tortoise", "Tommy")
a_zoo.list_animals()

a_zoo.list_animals.__doc__ # To view the docstring for the method
```

## Subclassing

In the previous example, we used strings to define an animal. Let's be more detailed in what an animal is by defining an `Animal` class.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)
```

    

# Additional Reading

1. [An Introduction to Python Classes and Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)