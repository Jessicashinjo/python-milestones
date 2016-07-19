# Data Serialization

Serialization is the process of coverting in-memory objects into a format that can be either (a) transmitted over the wire via an HTTP request, or (b) stored in a file for access later. You already have experience with this in JavaScript with the `JSON.parse()` and `JSON.stringify()` methods.

`JSON.stringify()` serializes a JavaScript object into a string that can be sent over HTTP.

`JSON.parse()` deserializes a string of characters back into an in-memory JavaScript object.

In Python, you can use the `pickle` module to accomplish the same thing.

## Using pickle

It's a straightforward process. You use `dump()` and `load()`.

```python
import pickle

interests = {
    "Sarah": ["MMA", "Fencing", "Writing"],
    "Michael": ["Hockey", "Gardening", "Cosplay"]
}

with open('serialized-interests', 'wb') as f:
  pickle.dump(interests, f)

with open('serialized-interests', 'rb') as f:
  deserialized = pickle.load(f)
  print(deserialized)
```

## Additional Resources

* [Dive into Python: Serialization](http://www.diveintopython3.net/serializing.html)
* [Python object serialization](https://docs.python.org/3.3/library/pickle.html)