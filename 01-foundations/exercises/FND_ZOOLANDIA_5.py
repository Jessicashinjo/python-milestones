# Zoolandia - Habitats

## Setup

```bash
cd ~/workspace/python/exercises/zoolandia
```

## Instructions

For this last Zoolandia exercises for the Foundations Milestone, you need to define all of the Habitats in which all of the animals live. You'll use the [aggregation](../resources/FND_INHERIT_COMPOSE_AGGREGATE.md#aggregation) pattern to assign animals to each Habitat.

In this example code, create the parent `Habitat` class that all others will derive from, and since every habitat in my Zoo will have animals in it, each specific habitat class will inherit that `inhabitant` property.

In the derived class, inherit from `Habitat`, and implement the `Aquarium` class. Define if the aquarium is freshwater or saltwater, and create a property that holds list of employees who are responsible for being in the tank with the animals.

##### Example Habitat Class

```python
class Habitat(object):

    def __init__(self, name, inhabitant):
        self.name = ""
        self.inhabitant = []


class Aquarium(Habitat):

    def __init__(self, name, saltwater, employees)
        Habitat.__init__(self, name, inhabitant)
        self.employees = []
        self.saltwater = saltwater
        ```

Once you have defined all of your habitats, write logic to output the name of each habitat, and the name of each animal it contains to the command line.

##### Example CLI Output

```bash
Habitat: Aquarium
   Dolphin
   Yellow Shark
   Octopus

Habitat: Savannah
   Giraffe
   Zebra
   Hippopotamus
```
