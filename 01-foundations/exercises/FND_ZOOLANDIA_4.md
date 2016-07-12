# Zoolandia - Multiple Inheritance

## Setup

```bash
cd ~/workspace/zoolandia
git checkout -b version-6
```

## Instructions

Your job is to think about additional classes that can be inherited by groups of your classes. Think about the examples that you were shown in live-coding.

* Canines
* Ambulatory
* Insect
* Swimming
* etc...

```python
class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species

class Flying:
    def __init__(self, wings = 2):
        self.wings = wings

class Dragonfly(Animal, Flying)
    def __init__(self, name, species):
        Animal.__init__(name, species)
        Flying.__init__(4)
```
