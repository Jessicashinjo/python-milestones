#Zoolandia - Specializing Derived Classes

## Setup

```bash
mkdir -p workspace/python/exercises/zoolandia && cd $_
git checkout -b version-2
```

## Instructions

### Override

1. Choose one of the general methods that you created in the `Animal` class for overriding.
1. Override that method in all of your species classes, giving each a more specialized implementation. For example, the species may only eat certain kinds of food, or have a limit on how much food can be eaten.
1. Make sure you invoke the parent class' overridden method with the `super` reference (e.g. `super(speciesClass, self).sleep()`);
1. Remember you can pre-filter or post-filter the data sent to/returned from the parent class' method.

### Constructors

1. Create a class for each of your animals. The class should, at the very least, set the initial name of all animals of that type to a name of your choosing.

  ```python
  class MyAnimal(speciesClass):
      def __init__(self)
          self.name = "Moopsie"
  ```

2. Use `print()` to output the name of each of your animal instances.

  ```python
  animalInstance = MyAnimal()
  print(animalInstance.name)
  ```
