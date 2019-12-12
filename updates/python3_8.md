---
layout: default
nav_exclude: true
---

# Python 3.8
{: .no_toc }

* 
{:toc}

Back to [Updates](../updates/)

---

Python 3.8 was released on October 14, 2019. Everything in the book should still work as it's written, except you might need to [install a specific version of Pygame](). Still, there's a bit more you might want to know about new Python releases. Here's a brief summary, including some links to official Python documentation. If you plan to continue using Python, it's a good idea to know what to look for in new releases.

## Overview

Every programming language evolves, and you see this in new *releases*. Python uses the [semantic versioning](https://semver.org) convention to name releases. This means Python is on major version 3, minor version 8, and patch version 0.

There are new features in Python 3.8, but there's nothing that should affect programs written in Python 3.7. That is, any program that works on Python 3.7 should work in Python 3.8 as well. The only exception is in situations where your program depends on an external library, and that library hasn't been updated to work with Python 3.8 yet.

[top](#top)

## What's new?

Python is a pretty stable language, so most of the new features involve more advanced usage. If you're curious to see the official release notes, here's the [Python Insider blog post](https://blog.python.org/2019/10/python-380-is-now-available.html) announcing the release, the [list of new features](https://www.python.org/downloads/release/python-380/), and the [documentation summary](https://docs.python.org/3/whatsnew/3.8.html) for the new features.

If you want a friendly but more detailed description of what's listed here, [Real Python](https://realpython.com/python38-new-features/) has a great summary with examples of each new feature.

### Assignment Expressions

Assignment expressions allow you to assign a value to a variable, while also returning that value. It's amusingly called the *walrus operator*, because the symbol for the expression is `:=`, which looks like a pair of walrus tusks.

For a quick example, here's how you'd assign a value to a variable, and then use that variable in a call to `print()`:

```python
name = 'Eric'
print(f"Hello, {name}!")
```

With assignment expressions, you can do this in one line:

```python
print(f"Hello {(name:='Eric')}!")
```

This is an overly simplified example, and it makes the code less readable for many people. But there are cases where this kind of behavior makes code much more concise, and when experienced programmers are familiar with this expression it becomes quite useful.

### Positional-only Arguments

If you've worked through Chapter 8, you learned about function arguments. Python allows you to use positional arguments, keyword arguments, or some mix of the two when you call a function. When you write a function, you can now specify that people can only call the function using positional arguments.

For example, consider the following function:

```python
def greet_user(name):
    print(f"Hello, {name}!")
```

This function can be called two ways:

```python
greet_user('eric')
greet_user(name='eric')
```

A forward slash specifies that the function can only be called with a positional argument:

```python
def greet_user(name, /):
    print(f"Hello, {name}!")
```

Now if people call the function using a keyword argument, they will receive an error.

This is useful for programmers developing APIs, where you may not want the parameter names to be public. It also allows you to change the parameter names at a later time, without breaking anyone else's code.

### Other New Features

- There are a number of new math functions in the Python standard library.
- Python allows you to specify the type of some variables, and the options for this have been expanded.
- The language has been optimized to make better use of available memory.

[top](#top)

## Should I upgrade?

- If you want to try any of the new features described above, you'll need to upgrade to Python 3.8. 
- If you aren't interested in trying any of the new features, there is no need to upgrade.
- If you are just starting out and haven't installed Python yet, go ahead and install Python 3.8. That's what will happen by default now, so you shouldn't need any special instructions to do this.

[top](#top)

## How do I upgrade?

The instructions are slightly different for some operating systems.

### Windows and macOS

You can download and run the official installer from [python.org](), just as you probably did to install Python originally. The new version will be installed alongside your previous version. Your Python command, which is probably either `python`, `python3`, or `py`, should be updated to point to Python 3.8.

If you've installed any external libraries such as Requests, you'll need to reinstall it, because Python 3.8 won't have access to any previously-installed libraries. For most packages, this means using pip again:

```
$ python -m pip install --user requests
```

Since your `python` prompt now points to Python 3.8, this will install the version of Requests that's compatible with Python 3.8.

### Linux

If you're on an apt-based system, the `deadsnakes` package has already been updated to include Python 3.8. If you haven't already used `deadsnakes`, add it to your system:

```
$ sudo add-apt-repository ppa:deadsnakes/ppa
```

Now update your system and install Python 3.8:

```
$ sudo apt-get update
$ sudoo apt install python3.8
```

You should now be able to use the command `python3.8` to run programs using the Python 3.8 interpreter. You'll also need to update your text editor to use this command.

If you've installed any external libraries such as Requests, you'll need to reinstall it, because Python 3.8 won't have access to any previously-installed libraries. For most packages, this means using pip again:

```
$ python3.8 -m pip install --user requests
```

This will install the version of Requests that's compatible with Python 3.8.

[top](#top)