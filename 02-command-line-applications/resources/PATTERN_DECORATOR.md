# Decorator Pattern

This pattern is for changing the behavior of an object instance dynamically, without affecting the behavior of any other instances that are based on the same class.

```python
class Bear:
  """Base bear class from which all other bears will inherit common behaviors """
  def growl(self):
    print("Growl")

  def run(self):
    print("Running")

  def hibernate(self):
    pass


# The SalmonEater class acts like an interface that specific bear
# types can inherit from to get salmon on the diet
class SalmonEater:
    """Class for any derived class to inherit from in order
    to add salmon to the diet of the animal"""

  def __init__(self):
    try:
      self.diet.append('Salmon')
    except KeyError:
      self.diet = ['Salmon']


# Grizzly bear inherits from both of the above classes
class Grizzly(Bear, SalmonEater):
  """Class for creating a grizzly bear"""

  def __init__(self):
    self.diet = ['Moose']
    SalmonEater.__init__()

```

Next, I'll create three instances of grizzly bear.

```python
gerta = Grizzly()
george = Grizzly()
galahad = Grizzly()
```

A forest ranger captures one of the bears so that it can be tagged, and biometric information can be recorded. This data will allow her to monitor and help the local bear populuation better. We need to specify behavior on George, Galahad, or Gerta whenever they are captured and tagged.

This is where a decorator comes in.

## Base Decorator

You begin with a new base decorator class that implements the same interface as the base class that it is decorating. Our class is going to decorate any instance of `Bear` or its derived classes, so it will inherit from `Bear`.

Notice that a specific bear instance is passed into the constructor.


```python
class BearDecorator(Bear):

  def __init__(self, bear_instance):
    self._bear = bear_instance

  def growl(self):
    self._bear.growl()

  def run(self):
    self._bear.run()

  def hibernate(self):
    self._bear.hibernate()
```

## Derived (concrete) Decorator

The first concrete decorator you want to define is one that will transmit data when a specific bear growls. This behavior can be added at any time during the execution of your code. You don't want this behavior on all bears, so you won't add the behavior via subclassing, nor through using a built-in decorator.

```python
class TransmitsGrowl(BearDecorator):
  """A decorator class that transmit information when
  the bear growls
  """

  def __init__(self, bear_instance):
    super().__init__(bear_instance)

  def growl(self):
    self._bear.growl()
    self.transmit("Growled")

  def transmit(self, data):
    print("Transmitting: {0}".format(data))
```

Now I can decorate Gerta.

```py
>>> gerta = Grizzly()
>>> george = Grizzly()
>>> galahad = Grizzly()
>>> 
>>> gerta = TransmitsGrowl(gerta)
>>> gerta.growl()
Growl
Transmitting: Growled
>>> gerta.run()
Running
```

## More Decoration

Let's define another concrete decorator that, when applied to an object instance, will also transmit the speed of the bear when it runs. Previously, when a bear was running, it simply printed "Running" to the console.

```py
class TransmitsSpeed(BearDecorator):
  """A decorator class that transmit speed information when
  the bear runs
  """

  def __init__(self, bear_instance):
    super().__init__(bear_instance)

  def run(self):
    self._bear.run()
    self.transmit("Running")

  def transmit(self, data):
    print("Transmitting: {0}".format(data))
```

Decorate George with the `TransmitsSpeed` class.

```py
>>> george = TransmitsSpeed(george)
>>> george.growl()
Growl
>>> george.run()
Running
Transmitting: Running
```

If needed later, you could then further decorate George with the `TransmitsGrowl` class, and it would be decorated with both behaviors.

```sh
>>> george = TransmitsGrowl(george)
>>> george.growl()
Growl
Transmitting: Growled
>>> george.run()
Running
Transmitting: Running
```
