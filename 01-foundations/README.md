# Setup

See if Python is installed.

```bash
which python
```

Check which version is installed. Most likely it will be version 2.7.x.

```bash
python --version
```

We're going to be learning version 3 of Python, and then later in the course, talk about differences between 2 and 3, because there is still a lot of version 2 code out in the wild and you will likely need to work with it.

## Managing versions

### Pyenv

#### OSX

OSX users, you should have Homebrew installed at this point. If you don't, do it now. Then run these commands in order.

```bash
brew install pyenv
pyenv install 3.3.6
md /workspace/hellopython && cd $_
touch hello.py
subl .
```

# Windows

The [venv](https://docs.python.org/3/library/venv.html#module-venv) was released with Python 3.3 to give Windows user the ability to execute different versions of Python.

## Hello, world

We're going to do the traditional `Hello, world` program to start off. Put the following code in `hello.py`.

```python
print "Hello!"
print "Is it me you're looking for?"
```

In the CLI, execute the following command.

```bash
python hello.py
```

## Python interpreter

You can use the CLI interpreter to enter and run some code that you just want to test out without having to put it in a file and running it.

```
╰─$ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> i_am_awesome = True
>>> if i_am_awesome:
...   print "bow down to me"
... 
bow down to me
```

## Pip

Pip is, by far, the most common way for [Python packages to be installed](https://packaging.python.org/en/latest/installing/#use-pip-for-installing). Take some time, by follow the previous link, to review how to properly use pip to install packages