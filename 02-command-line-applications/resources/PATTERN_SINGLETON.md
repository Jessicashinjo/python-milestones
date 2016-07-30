# Singleton Pattern

A common pattern in software development is **Singleton**. It is useful when you only need one instance of an object to be used throughout the entire system. Developers often implement singletons for a class that is used as a utility - or helper - to many aspects of the system.

## Singleton Class

One example is a logging class. Let's look at an example **LogWriter** class that is a singleton. It has one, simple function: take a string input and log that string to a file. Since this is a helper function that can be used by any other object instance, there is no reason to create multiple instances of this class, thereby using memory unnecessarily.

```python
from datetime import datetime
from time import time

class LogWriter:
  """This class takes any string of characters and writes them
  to a log file.

  Methods:
    log -- Logs a message to a file
  """

  _logInstance = None

  # Singleton pattern. There should only be one instance of
  # LogWriter used in the application.
  # 
  # The __new__ method is different from __init__. It's resposibiity
  # is the creation of a new instance of a class. __init__ runs after
  # that and it responsible for initializing the new instance with
  # properties, if needed.
  def __new__(class_, *args, **kwargs):
    if not isinstance(class_._logInstance, class_):
        print('Creating a new LogWriter instance')
        class_._logInstance = object.__new__(class_, *args, **kwargs)
    return class_._logInstance


  def log(self, message):
    """Log a message to the log file

    Argments:
      message -- Any string
    """
    with open('messages.log', 'a+') as logger:
      timestamp = time()
      logger.write("{0}: {1}\n".format(
        datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
        str(message)
      ))
```

Now that it's a singleton, it doesn't matter how many times I initialize an instance, the same one is used.

```python
>>> from logwriter import *
>>> logger = LogWriter()
Creating a new LogWriter instance
>>> another_logger = LogWriter()
>>> logger.log("All shapes created")
```

Notice how the `print()` method only executed the first time I created an instance, not the second time.

## Singleton Module

Now that we've looked at the traditional Singleton pattern, there's actually a more Pythonic way to have a singleton... a module.

Since a module only gets imported once per session, then our logging utility could very easily just be a module with one function in it. To show that it only gets imported once, I added a global variable to the module, and each time a message is logged, I increment the count by 1.

If it got imported more than once, every time I called the `log()` method, the `count` variable would be reset to 1.

##### logging.py

```python
from datetime import datetime
from time import time

count = 0

def log(message):
  """Log a message to the log file

  Argments:
    message -- Any string
  """
  global count
  count += 1
  print(count)
  with open('messages.log', 'a+') as logger:
    timestamp = time()
    logger.write("{0}: {1}\n".format(
      datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
      str(message)
    ))
```

If you log multiple messages, you'll see the counter increment.

```python
>>> log("Message #1")
1
>>> log("Message #2")
2
>>> log("Message #3")
3
>>> log("Message #4")
4
>>> log("Message #5")
5
>>> log("Message #6")
6
>>> log("Message #7")
7
>>> log("Message #8")
8
```