# Types and Objects

Everything is an object in Python.

```
>>> type(True)
<class 'bool'>
>>> type(1)
<class 'int'>
>>> def test():
...   print("hello, world")
... 
>>> type(test)
<class 'function'>
>>> type(humansizes)
<class 'module'>
>>> dictionary = { "color":"blue", "size":9090 }
>>> type(dictionary)
<class 'dict'>
>>> atuple = ( "blue", 9090 )
>>> type(atuple)
<class 'tuple'>
>>> reindeer = ["dasher", "dancer", "prancer", "vixen", "olive"]
>>> type(reindeer)
<class 'list'>
>>> boy_bands = { "nsync", "one direction", "boyz II men" }
>>> type(boy_bands)
<class 'set'>
```