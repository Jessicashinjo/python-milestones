# Mathmagician

## Setup

```
mkdir -p ~/workspace/python/exercises/cli && cd $_
touch mathmagician.py
```

## Instructions

### Step 1

Write your unit tests to reflect what classes, methods, and I/O is expected for each feature.

### Step 2

Your program will have one class with a **minimum** of three methods on it:

1. `print_integers(self)`
1. `print_fibonacci(self)`
1. `print_primes(self)`

Write unit tests that will verify the output of each method. Do not write any implementation code until you have a unit test for each method that fails.

### Step 3

Create a simple implementation of a console application that displays a prompt to the user, and listens for a key press.

1. Use `print()` to output the message `Press any key to exit`.
1. Use `input` to accept user input, so that when your program runs, you press a key and it exits.

### Step 4

Now you'll write the implementation code for your three methods, and the operation of the program itself.

1. You want it to do one of three mathematical operations. Update your prompt to be *I am the Math Magician. What would you like me to do?* The options will be Fibonacci, Primes, or Integers.
    
    ```
    user_choice = input('I am the Math Magician. What would you like me to do? ')
    ```
1. The goal here is that once the user tells the program what operation to perform, it will spit out the numbers forever until you “ctrl+c”.
  `print(“Ok. I’m going to help produce " + user_choice);`
1. Use `time.sleep(seconds)` when you output each number to the console to make each number legible (otherwise it goes too fast).
1. Make sure that your code validates user input. As a software developer, part of your job will be to handle edge cases. Think about possible things that the user can do that don't match what you expect of them, because they will. For example, at the prompt, they could type in the string `Integers`.

### Step 5

Document your implementation code with docstrings.
