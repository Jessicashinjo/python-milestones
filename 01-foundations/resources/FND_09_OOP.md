# Object Oriented Programming

There are four tenets of object oriented programming, and you encountered all of them during your experience with JavaScript, which itself is an object oriented language.


## Inheritance with Classes

We taught you in the front end course how to handle inheritance in JavaScript with the prototypal style. In Python, you inherit with classes.

```python
class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def setSpecies(self, species):
        self.species = species

    def getSpecies(self):
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")
```


## Polymorphism

[Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)) means that different objects may share the same set of properties and methods, but each may use those properties and methods to achieve different behavior.

For example, in your base class of Animal, you define a general rule of how fast an Animal can walk. However, in the derived Lizard class, you can override that rule to give Lizards a slightly different behavior. For every leg they have, they can move twice as fast as a generic Animal.

```python
class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0

    def getName(self):
        return self.name

    def setLegs(self, number_of_legs):
        self.legs = number_of_legs

    def walk(self):
        print("Parent class walk method")
        self.speed = self.speed + (0.1 * self.legs)

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")

    # Override the parent method to add more functionality
    def walk(self):
        self.speed = self.speed + (0.2 * self.legs)
```

In Python, you use the `super()` method, which allows a derived class to invoke the corresponding method in the parent class, possibly modifying its inputs or outputs before returning.

```python
class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species

    def eatFood(self, food):
        return "{0} eats {1}".format(self.name, food)

class Panda(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Panda")

    def eatFood(self, food):
        parent_message = super(Panda, self).eatFood(food)
        message = ' '.join(parent_message, "but doesn't digest it very well")
        return message
```


## Encapsulation

The encapsulation concept is all about defining what data needs to be manipulated, defining the methods that need to be exposed to manipulate the data, and then hiding the internal representation of that data. Our current code encapsulates all of the functionality needed to create a basic animal and make it walk.

However, we hide the implementation of setting the speed of the animal since we want to control how it is set based on the simple algorithm in the `walk()` method.  That's called Information Hiding because no external actor (i.e. code) can access, or set, the walking speed of the animal. It can only specify the number of legs that the animal has.


## Abstraction

As your code becomes more complex, Abstraction is the process that you, the developer, will go through to provide the most general, and hopefully simplest, way possible. This is done via multiple refactors of your code as complexity slowly works its way in.

With our current code, the `Animal` class is an abstraction of more specific animals that we create later, such as the Lizard.


## Resources
* https://en.wikipedia.org/wiki/Object-oriented_programming

