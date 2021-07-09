---
layout: default
nav_exclude: true
parent: Updates
nav_order: 1000
---

# Python 3.9
{: .no_toc }

* 
{:toc}

Back to [Updates](../updates/)

---

Python 3.9 was released on October 5, 2020. Everything in the book works in the latest printing. Still, there's a bit more you might want to know about new Python releases. Here's a brief summary, including some links to official Python documentation. If you plan to continue using Python, it's a good idea to know what to look for in new releases.

## Overview

Every programming language evolves, and you see this in new *releases*. Python uses the [semantic versioning](https://semver.org) convention to name releases. This means Python is on major version 3, minor version 9, and patch version 6.

There are new features in Python 3.9, but there's nothing that should affect programs written in Python 3.8. That is, any program that works on Python 3.8 should work in Python 3.9 as well. The only exception is in situations where your program depends on an external library, and that library hasn't been updated to work with Python 3.9.

[top](#top)

## What's new?

Python is a pretty stable language, so most of the new features involve more advanced usage. A good place to look for what's new in the latest release is in the official [What's New in Python 3.9](https://docs.python.org/3/whatsnew/3.9.html) article from python.org. If you want even more detailed information about what's changed, see the official [release notes](https://docs.python.org/release/3.9.6/whatsnew/changelog.html#changelog).

If you want a friendly but more detailed description of what's listed here, [Real Python](https://realpython.com/python39-new-features/) has a great summary with examples of each new feature.

### Combining Dictionaries

New ways of combining dictionaries have been added. For example if we have two dictionaries called `my_pets` and `your_pets`, we can combine them with the `|` operator to get a new dictionary that combines the two:

```python
>>> my_pets = {'dog': 'willie', 'cat': 'henry'}
>>> your_pets = {'snake': 'samantha', 'scorpion': 'minca'}
>>> our_pets = my_pets | your_pets
>>> our_pets
{'dog': 'willie', 'cat': 'henry', 'snake': 'samantha', 'scorpion': 'minca'}
```

If the same key exists in both dictionaries, the value from the second dictionary in the combination statement is used.

### Removing prefixes and suffixes from strings

If you want to remove a prefix or suffix from a string, you can use the new `str.removeprefix(prefix)` and `str.removesuffix(suffix)` methods:

```python
>>> filename = 'pcc_2e_cover_image.png'
>>> filename.removesuffix('.png')
'pcc_2e_cover_image'
```

### Other New Features

- There is a new module called `zoneinfo` that improves support for working with timezones.
- A new module called `graphlib` improves support for working with graphs ('graph' here means a collection of nodes and edges, for example the kind that's used to model a network).

[top](#top)

## Should I upgrade?

- If you want to try any of the new features described above, you'll need to upgrade to Python 3.9. 
- If you aren't interested in trying any of the new features, there is no need to upgrade.
- If you are just starting out and haven't installed Python yet, go ahead and install Python 3.9. That's what will happen by default now, so you shouldn't need any special instructions to do this.

[top](#top)

## How do I upgrade?

The instructions are slightly different for some operating systems.

### Windows and macOS

You can download and run the official installer from [python.org](), just as you probably did to install Python originally. The new version will be installed alongside your previous version. Your Python command, which is probably either `python`, `python3`, or `py`, should be updated to point to Python 3.9.

If you've installed any external libraries such as Requests, you'll need to reinstall it, because Python 3.9 won't have access to any previously-installed libraries. For most packages, this means using pip again:

```
$ python -m pip install --user requests
```

Since your `python` prompt now points to Python 3.9, this will install the version of Requests that's compatible with Python 3.9.

### Linux

If you're on an apt-based system, the `deadsnakes` package has already been updated to include Python 3.9. If you haven't already used `deadsnakes`, add it to your system:

```
$ sudo add-apt-repository ppa:deadsnakes/ppa
```

Now update your system and install Python 3.9:

```
$ sudo apt-get update
$ sudoo apt install python3.9
```

You should now be able to use the command `python3.9` to run programs using the Python 3.9 interpreter. You'll also need to update your text editor to use this command.

If you've installed any external libraries such as Requests, you'll need to reinstall it, because Python 3.9 won't have access to any previously-installed libraries. For most packages, this means using pip again:

```
$ python3.9 -m pip install --user requests
```

This will install the version of Requests that's compatible with Python 3.9.

[top](#top)