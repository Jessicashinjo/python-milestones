# Mathmagician

## Setup

1. Create a new Visual Studio console solution named *MathMagician*.
1. Create a matching project in your solution for unit tests (i.e. *MathMagicianTests*).

## Instructions

**Write your unit tests first**

### Step 1

Your program will have one class with three methods on it:

1. `printIntegers()`
1. `printFibonacci()`
1. `printPrimes()`

Write unit tests that will verify the output of each method. Do not write any implementation code until you have a unit test for each method that fails.

### Step 2

Create a simple implementation of a console application that displays a prompt to the user, and listens for a key press.

1. Use `Console.WriteLine()` to output the message *Press any key to exit*.
1. Use [`Readkey`](https://msdn.microsoft.com/en-us/library/system.console.readkey(v=vs.110).aspx), so that when your program runs, you press a key and it exits.

### Step 3
Now you'll write the implementation code for your three methods, and the operation of the program itself.

1. We want it to do one of three mathematical operations. Update your prompt to be *I am the Math Magician. What would you like me to do?* The options will be Fibonacci, Primes, or Integers.
1. Then to get the user to choose. `string = desiredMathProcess = Console.ReadLine ();`
1. The goal here is that once the user tells the program what operation to perform, it will spit out the numbers forever until you “ctrl+c”.
  `Console.WriteLine(“Ok. I’m going to help produce " + Choice);`
1. Create the following three methods in your project:
1. Use `Thread.Sleep(500)` when you output each number to the console to make each number legible (otherwise it goes too fast).
