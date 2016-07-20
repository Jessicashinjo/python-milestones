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

When you type in a command in the terminal, the shell looks in certain places to find a matching executible file to run.  Those places are listed in what's called the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)).  Since our `hello.sh` isn't in the PATH, it can't be run by simply typing its name into the terminal, even though we're in the same directory as the script.

To run the script, we need to provide the path to it.  You can use an absolute path such as `/Users/ryan/workspace/python/resources/bash_scripts/hello.sh`, which can be rather clunky, or relative path, which, if you're in the same directory will look like `./hello.sh`.  The dot `.` is the current directory, much like `..` is the parent directory, as you've likely used in the command `cd ..`.  Thus `./hello.sh` says "run the script `hello.sh` in the current directory."


#### Variables and Logic
```bash
#!/bin/bash

greeting='Hello'

if [ "$1" ]; then
  echo $greeting $1!
else
  echo $greeting World!
fi
```
