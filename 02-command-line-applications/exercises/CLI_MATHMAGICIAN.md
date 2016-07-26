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

Your program will have one class with a **minimum** of three methods on it. Each method should also accept an argument that determines how many numbers in the corresponding sequence should be generated.

1. `generate_integers(self, number_to_output)`
1. `generate_fibonacci(self, number_to_output)`
1. `generate_primes(self, number_to_output)`

You decide what type of collection that each of those methods should produce. Write unit tests that will verify the output of each method. Do not write any implementation code until you have a unit test for each method that fails.

### Step 3

Next, build the menu that the user will see when your module is executed.

```sh
I am the Math Magician. What would you like me to do?

1. List prime numbers
2. Show fibonacci sequence
3. List integers
4. Quit
```

### Step 4

Now you'll write the implementation code for your three methods, and the operation of the program itself.

1. When the user picks a sequence to generate, then ask how many number of the sequence should be printed.
1. Use `time.sleep(seconds)` when you output each number to the console to make each number legible (otherwise it goes too fast).
1. Make sure that your code validates user input. As a software developer, part of your job will be to handle edge cases. Think about possible things that the user can do that don't match what you expect of them, because they will. For example, at the prompt, they could type in the string `Integers`.

### Step 5

Document your implementation code with docstrings.
