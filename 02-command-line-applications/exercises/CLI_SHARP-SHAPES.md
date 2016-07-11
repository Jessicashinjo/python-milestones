# Sharp Shapes

## Setup

```
mkdir -p ~/workspace/python/exercises/cli && cd $_
touch sharpshapes.py
```

## Instructions

This exercise involved creating a system that generates myriad shapes. Build a command line tool that does the following:

1. Outputs a numbered list of possible shapes to be built.
1. Allow user to select one of the choices.
1. After shape type is chosen, ask for size information.
    1. Radius for circles.
    1. Width/height for squares and rectangles.
    1. Radius/height for cylinders.
    1. etc..
1. After basic size information is entered, the program will output circumference/area/volume of the shape, and the number of sides for the shape.

##### Step 1 Example

```bash
Select a shape:
1. Circle
2. Square
3. Rhombus
4. Cube
5. Cylinder
> 
```

##### Step 2 Example

```bash
You chose Cube.

Enter the height, width, and depth separated by commas
> 5,4,8
```


##### Step 3 Example

```bash
The total volume of the cube is 160.
```


## Requirements

**Write your unit test suite first.** 

Start with a basic Shape class. Then plan out every specific shape that you want to derive from it, write tests verifying type checking, and the expected output of every method on your shapes.

##### Example starter tests

```python
import unittest
from shape import Shape

class TestSharpShapes(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')

    def test_shape_type(self):
        simple = Shape()

        assertIsInstance(simple, Shape);

    def test_shape_area(self):
        simple = Shape()
        simple.width = 2
        simple.height = 2
        
        assertEqual(simple.calculate_area(), 4);
```


> **More info about the math:** http://mathworld.wolfram.com/
