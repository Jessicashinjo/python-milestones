# Zoolandia 1 - Defining Your Favorite Species

## Setup

```bash
mkdir -p workspace/python/exercises/zoolandia && cd $_
git checkout -b version-1
touch zoolandia.py
```

## Instructions

1. Create the Animal class. Create some simple properties and methods on Animal. You are going to create some derived classes that inherit from Animal, so make sure that the properties/methods you add are general to **all** Animals (e.g. name, height, weight, etc).

    ##### Example property/method definition

    ```python
    class Animal(object):

      def __init__(self, name, height, weight):
          self.name = name
          self.species = height
          self.species = weight

      def get_name(self):
          return self.name

      def get_height(self):
          return self.height

    ```

1. After you are happy with your Animal class, create a derived class that defines a particular species of Animal. Create some properties that apply **only** to that species.

    ```python
    # The species for a Red Panda
    class AilurusFulgens(Animal):

        # Define simple properties for a Red Panda here

    ```

1. Create three more classes for species of animals of your choosing. Wikipedia is a great tool to discover species names.
1. Create some instances of your species.
1. Assign values to the properties of each.
1. Use `print()` to output the property values of your animals to the console.
