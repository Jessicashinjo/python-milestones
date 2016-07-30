# Factory Pattern

The factory pattern in software development is used to create one of myriad types of objects without having to actually specify which class definition is going to be used. It's true power is when the construction of each object has some complexity that isn't obvious or straightforward.

It is strongly used in statically typed languages like Java and C# so that different, but sibling, derived types can be created without knowing all of the different class names.

However, the pattern is just as useful in Python.

#### Example

First, if you are using a version of Python < 3.4, you are going to need to `pip install enum34` in order to run this code. This is just a module, so that our factory for creating bears is a singleton in the rest of application.

This example is just to show you the pattern, and is a fairly simplistic implementation. Since some of the bears need to have their hair color passed in as a list during construction, and others don't, a factory can be used to ease in the creation of bears by other code modules.

##### bearfactory.py

---

```python
from enum import Enum

# Bear enumeration that can be used to specify the
# kind of bear needed
Bears = Enum(
  'Bears',
  'PANDA KODIAK GRIZZLY BROWN BLACK POLAR'
)

class Bear:
  def __init__(self, colors):
    self.hair_colors = colors


class KodiakBear(Bear):
  def __init__(self, colors):
    super().__init__(colors)

  def __str__(self):
    return "Kodiak bear"


class BlackBear(Bear):
  def __init__(self, colors):
    super().__init__(colors)

  def __str__(self):
    return "Black bear"


class PolarBear(Bear):
  def __init__(self, colors):
    super().__init__(colors)

  def __str__(self):
    return "Polar bear"


class PandaBear(Bear):
  def __init__(self, colors):
    super().__init__(colors)

  def __str__(self):
    return "Panda bear"


class BrownBear(Bear):
  def __init__(self):
    self.hair_colors = ['Brown']

  def __str__(self):
    return "Brown bear"


class GrizzlyBear(BrownBear):
  def __init__(self, colors):
    super().__init__(colors)
    self.hair_colors.extend(['Gold', 'Grey'])

  def __str__(self):
    return "Grizzly bear"


def create(bear_type):
  """Creates an instance of a bear. Possible types are specified
  in the Bears enum, which can be imported from this module

  Arguments:
    bear_type -- One of the types in the Bears enumeration
  """

  bear = None
  global Bears

  if bear_type == Bears.BROWN:
    bear = BrownBear()

  elif bear_type == Bears.BLACK:
    bear_type = BlackBear(['Black'])

  elif bear_type == Bears.PANDA:
    bear_type = PandaBear(['White', 'Black'])

  elif bear_type == Bears.KODIAK:
    bear_type = KodiakBear(['Orange', 'Blonde'])

  elif bear_type == Bears.POLAR:
    bear_type = PolarBear(['White'])

  elif bear_type == Bears.GRIZZLY:
    bear_type = GrizzlyBear()

  else:
    raise Exception("Specified bear type type not found")

  return bear_type
```

Then start using the factory.

##### p.py

---

```python
Factory = __import__('bearfactory')

kodiak = Factory.create(Factory.Bears.KODIAK)
print("{0}: {1}".format(str(kodiak), ", ".join(k for k in kodiak.hair_colors)))
```