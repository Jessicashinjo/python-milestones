# Mathmagician

## Setup

```
mkdir -p ~/workspace/python/exercises/cli && cd $_
touch mathmagician.py
```

## Instructions

**Write your unit tests first**

### Step 1

Your program will have one class with three methods on it:

1. `print_integers()`
1. `print_fibonacci()`
1. `print_primes()`

Write unit tests that will verify the output of each method. Do not write any implementation code until you have a unit test for each method that fails.

### Step 2

Create a simple implementation of a console application that displays a prompt to the user, and listens for a key press.

1. Use `print()` to output the message `Press any key to exit`.
1. Use `input` to accept user input, so that when your program runs, you press a key and it exits.

### Step 3
Now you'll write the implementation code for your three methods, and the operation of the program itself.

1. You want it to do one of three mathematical operations. Update your prompt to be *I am the Math Magician. What would you like me to do?* The options will be Fibonacci, Primes, or Integers.
    
    ```
    user_choice = input('I am the Math Magician. What would you like me to do?')
    ```
1. The goal here is that once the user tells the program what operation to perform, it will spit out the numbers forever until you “ctrl+c”.
  `print(“Ok. I’m going to help produce " + user_choice);`
1. Create the following three methods in your project:
1. Use `time.sleep(seconds)` when you output each number to the console to make each number legible (otherwise it goes too fast).
