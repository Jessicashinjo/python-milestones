# Unit Testing

You got an introduction to unit testing during your front end course work. On the server side, unit testing becomes easier, and more straightfoward because you don't have user interfaces to worry about. No functional testing at all.

Server side code is all about constrained inputs and verifiable outputs. Perfect for unit testing.

Read a [walkthrough of setting up unit tests](https://docs.python.org/3.5/library/unittest.html) in Python.

Just like with Jasmine for your JavaScript, you should use your unit tests as part of your design stage. Write as many unit tests as you can for your initial classes and methods. Once you feel you have good coverage for the basic logic of your application, then you begin writing simple implementations of the code in order to make the tests pass.

## Example

Python provides its own unit testing framework named, appropriately, `unittest`. Here's a sample class for running unit tests.

① The test class must sub-class `unittest.TestCase`

② Each function in the class must start with `test_`

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```
