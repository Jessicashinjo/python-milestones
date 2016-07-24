# Bash Scripting

## Introduction

Bash is an acronym for [Bourne Again SHell](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), the default [shell](https://en.wikipedia.org/wiki/Unix_shell) for OS X and many other Linux distributions.  For those of you not using zsh (or another shell), all the commands you've ever typed into the terminal have been run by bash.

Bash scripts are, at their most basic, just a list of terminal commands stored in a file for easy execution.  The bash scripting language's power comes from its ability to run any terminal command or executable and capture its output, combined with logic constructs and data passing via variables.

#### Hello World Example
```bash
#!/bin/bash

echo Hello World!
```

In bash scripts a `#` is used to comment out a line, but the `#!` on the first line of a bash script is a special construct called a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)). This construct tells the program loader to use the following string (in this case `/bin/bash`) as a path to the interpreter to use to run the rest of the script.

`echo` is a command line application that returns any arguments passed to it to the terminal.  It works much like Python's `print()` or JavaScript's `console.log()`, here just printing the "Hello World!" that follows it.

## Running Scripts

In the terminal, make a new directory and `touch` a new file called `hello.sh`.  `.sh` is the common extension for shell script files and naming your file as such will enable syntax highlighting in most editors.  Open the file in your editor of choice and paste or type in the example script above.

Back in the terminal, try running the script by just typing its name.  You should see something like this: `bash: hello.sh: command not found`

When you type in a command in the terminal, the shell looks in certain places to find a matching executable file to run.  Those places are listed in what's called the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)).  Since our `hello.sh` isn't in the PATH, it can't be run by simply typing its name into the terminal, even though we're in the same directory as the script.

To run the script, we need to provide the path to it.  You can use an absolute path such as `/Users/bobert/workspace/python/resources/bash_scripts/hello.sh`, which can be rather clunky, or relative path, which, if you're in the same directory will look like `./hello.sh`.  The dot `.` is the current directory, much like `..` is the parent directory, as you've likely used in the command `cd ..`.  Thus `./hello.sh` says "run the script `hello.sh` in the current directory."

However running `./hello.sh` in the terminal will still result in an error: `bash: permission denied: ./hello.sh`!  Wait, we created this file, why don't we have permission to it?  Well, we _do_ have permission to read and write the file, but not to execute (run) it.  File permissions on Linux/Unix systems are fairly granular, with separate permissions for reading, writing, and executing a particular file.

You can check the permissions on a file by using the `ls` command with the `-l` flag for "long" which will show file permissions as well as ownership and modification date information.  Running the command `ls -l` in the same directory as our script should give output something like this: `-rw-r--r--  1 bobert  staff    0 Jul 20 14:00 hello.sh`

There are three permissions in order, `r`ead `w`rite e`x`ecute, in three groupings for owner, group, and everyone.  With that in mind, looking at the permissions on our `hello.sh` file you can see the permissions for owner are `rw-` for group are `r--` and everyone are `r--`.  Everyone can read, only we, as the owner, can write, and nobody can execute the file.  In order to be able to run our file, we'll have to change the permissions to enable execution.  The command for this is [`chmod`, short for _change mode_](https://en.wikipedia.org/wiki/Chmod).

`chmod` can accept [four octal digits](https://en.wikipedia.org/wiki/Chmod#Octal_modes) as an argument, which is outside the scope of this intro, but it also has useful flags for toggling specific permissions.  To make our file executable, the command is `chmod +x hello.sh`, which makes a bit of sense, as it's adding the e`x`ecute permission.  Running `ls -l` in the directory should now output something like `-rwxr-xr-x  1 bobert  staff    0 Jul 20 14:00 hello.sh`, and depending on your terminal the file name may have changed color to indicate that the file is now executable.

Now, with the executable flag set and using `./` to point to our file, we can run it and observe the output.
```
bash-3.2$ ./hello.sh
Hello World!
bash-3.2$
```

#### Takeaways
- To execute files you must set their execution permissions with `chmod +x filename.sh`
- You must call the file using its path i.e. `./filename.sh` if it's not in the PATH

## Variables and Logic

For more complex interactions, bash scripts support reading arguments from the terminal as well as setting and reading variables and logic constructs such as [if-else](http://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php#if) and [case](http://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php#case) statements.  Copy the code below into a new file `logic.sh`, chmod it and we'll give it a look:

```bash
#!/bin/bash

greeting=Hello

if [ $1 ]; then
  echo $greeting $1!
else
  echo $greeting World!
fi
```

As per the first example, we start the script with the shebang and path to bash.  The next line is a variable definition with the variable `greeting` initialized with the string value "Hello".  Like Python, variables in bash scripts don't need a keyword like `var` to be defined, unlike Python, strings can just be tossed in all willy-nilly without quotes, unless the string contains spaces.  Also of note, the lack of spaces between the variable, the equal sign, and the value.  In a bash script, those cannot have white space between them.  The line `greeting = Hello` would result in `line 3: greeting: command not found` and `greeting= Hello` would get `line 3: Hello: command not found`.

The next block of code is a bash if statement which opens with an `if` and ends with a `fi`.  (Likewise a case statement opens with `case` and closes with `esac`.)  The test is contained within square brackets, and followed by a `then`.  Ignoring the `$1` for a moment, you'll notice a semicolon between the if's test and the `then`.  In a bash script, each line is a new command, and a semicolon can be used to separate multiple commands on the same line.  Putting the `then` on the same line as the `if` is a convention for readability, as is indenting the code within the if statement.  The following two if statements are functionally identical to the one in the script above.
```bash
if [ $1 ]; then; echo $greeting $1!; else; echo $greeting World!; fi

if [ $1 ]
then
echo $greeting $1!
else
echo $greeting World!
fi
```
Several places in the script you can see words prefixed with a `$`, and as the `$greeting` may have clued you in, this is a bash scripts way of referencing variables.  A word prefixed by the `$` will be replaced with that variable's value, thus for this script `echo $greeting` would output `Hello`.

So what about that `$1` we never declared?  Bash scripts have what are called [positional parameters](http://tldp.org/LDP/abs/html/othertypesv.html) which are used to access arguments passed to the script on the command line when it is executed.  `$0` references the command itself, `$1` the first argument, `$2` the second, etc.  As an example, given a script `position.sh` that contains only the line `echo $0 $1 $2 $3` calling it with just `./position.sh` would output `position.sh` to the terminal.  Calling it with `./position.sh foo` gives `position.sh foo` etc.  For positional arguments over 9, curly braces are needed i.e. `${10}`, though you'll rarely if ever need to write a script that takes that many runtime arguments.  If you do, there's also the special variables `$*` and `$@` which grab _all_ the positional parameters.

Knowing about positional parameters, we can now evaluate the test in the if statement.  Since there's no comparison checking with a `==` or similar, this if clause only tests if `$1` exists, i.e., was `logic.sh` called with an argument.  Looking at the cases, in the `then` the `echo` prints `$greeting` a space `$1` and an exclamation point, while in the `else` it prints `$greeting` and " World!"  Notice that there is no string concatenation required in the output from `echo`, it prints exactly what follows it, replacing the variables with their content and printing all other characters as they are in the line.

With all the pieces in place, we can look at the script and see that if called with an argument `./logic.sh Bobert` it should print `Hello Bobert!` and if called without `./logic.sh` it should print `Hello World!`.

## Incorporating Python

As Python can be run from the terminal, you can use bash scripts to automate execution of your Python code.  A very simplistic example with a python file `simple.py`:
```python
print('World!')
```
and bash `script.sh`:
```bash
#!/bin/bash

python_output=`python simple.py`

echo 'Hello' $python_output
```

You've seen most of the content in the bash script before outside the execution of the Python code.  Sticking `python simple.py` on its own line in the script would run that exact command, telling the Python interpreter to run the `simple.py`, but it would immediately print that "World!" to the console as it was executed.  To capture the output of a program execution, the executable command needs to be wrapped in backticks.  Doing so on line three of the bash script sets the bash variable `python_output` to the _terminal output_ (i.e. printed data) of `simple.py`, so it can then be used later in the `echo` statement to build a full "Hello World!".

That's bringing Python output into a bash script, but what about the reverse?  Python has a [built in module `sys`](https://docs.python.org/3.3/library/sys.html) that enables access to command line arguments passed at execution time.  Its syntax looks much like the positional parameters from bash scripts, where the index number referenced in `sys.argv[]` corresponds to the argument number in the sent list of arguments.  In the following `sentargs.py` script, the `sys.argv[1]` grabs the first argument sent it and uses that in its output.

```python
import sys

def print_arg(argument):
    output = 'Hello ' + argument
    print(output)

print_arg(sys.argv[1])
```

With examples of setting bash script variables from Python output, and sending command line arguments into a Python script, we can now chain the `simple.py` and `sentargs.py` scripts together via this `chain.sh` bash script to sequentially assemble and print a "Hello World!".

```bash
#!/bin/bash

part_two=`python simple.py`

python sentargs.py $part_two
```
