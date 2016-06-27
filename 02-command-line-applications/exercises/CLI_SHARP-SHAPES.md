# Sharp Shapes

## Setup

1. Create a new Visual Studio solution named *SharpShapes*.
1. In your terminal, cd to the new solution directory and copy in the Visual Studio `.gitignore`.
1. Next, you must add a unit testing project to your solution. Read a [walkthrough of setting up unit tests](https://www.visualstudio.com/en-us/get-started/code/create-and-run-unit-tests-vs) in Visual Studio.

## Instructions

This exercise involved creating a system that generates myriad shapes in C#. Build a command line tool that does the following:

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

```
namespace SharpShapesTests
{
    [TestClass]
    public class Test
    {
        [TestMethod]
        public void TestShapeType ()
        {
            Shape simple = new Shape();
            Assert.IsInstanceOfType(simple, typeof(Shape));
        }

        [TestMethod]
        public void TestShapeArea ()
        {
            Shape simple = new Shape();
            simple.width = 2;
            simple.height = 2;
            Assert.IsTrue (simple.calculateArea () == 4);
        }

        [TestMethod]
        public void TestShapeVolume ()
        {
            Shape simple = new Shape();
            simple.width = 2;
            simple.height = 3;
            simple.depth = 5;
            Assert.IsTrue (simple.calculateVolume () == 30);
        }


    }
}
```


> **More info about the math:** http://mathworld.wolfram.com/
