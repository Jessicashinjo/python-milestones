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

## Lists

A list is like an array in JavaScript. Just an unordered, untyped collection of any values. The example below is storing strings, an integer, and even another list inside a list.

```python
junk = ['carrots', 'celery', 'kale', 2, ['peas', 'corn']] 
junk.insert(1, 'kidney beans')
junk.extend([True, 'tornado'])
junk.append('hurricane')
print(junk)
```