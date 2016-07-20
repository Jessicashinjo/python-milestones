# Bash Scripting

## Introduction

Bash is an acronym for [Bourne Again SHell](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), the default [shell](https://en.wikipedia.org/wiki/Unix_shell) for OS X and many other Linux distributions.  For those of you not using zsh (or another shell), all the commands you've ever typed into the terminal have been run by bash.

Bash scripts are, at their most basic, just a list of terminal commands stored in a file for easy execution.  The bash scripting language's power comes from its ability to run any terminal command or executable and capture its output, combined with logic constructs and data passing via variables.

####Hello World Example
```bash
#!/bin/bash

echo 'Hello World!'
```

The #! on the first line of a bash script is a special construct called a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) that tells the program loader to use the following interpreter (in this case `/bin/bash`) to run the rest of the script.


