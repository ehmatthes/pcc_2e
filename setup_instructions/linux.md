---
layout: default
title: Setting up Python on Linux
parent: Setup Instructions
nav_order: 3
---

# Setting up Python on Linux
{: .no_toc }

* 
{:toc}

---

## Checking your current version of Python

Python is installed by default on most modern Linux systems, so let's see what you have installed. Open a terminal and issue the following command:

```bash
$ python --version
Python 3.7.2
```

You might see something different, such as `Python 2.7.15`. If that's the case, try the same command using **python3**:

```bash
$ python3 --version
Python 3.7.2
```

 You'll need Python 3.6 or higher to follow along with the book. If you see a version earlier than Python 3.6, or if you see an error message, it's fairly straightforward to install a newer version of Python.

## Installing Python 3.7

The following will work for apt-based systems. We'll install a package called deadsnakes, which you can use to install just about any version of Python that's been released, and you can install as many versions as you like.

Open a terminal and enter the following commands:

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt install python3.7
```

This should install Python 3.7 on your system, and you can start a Python session with the command **python3.7**:

```bash
$ python3.7
Python 3.7.2 (default, Dec 27 2018, 04:01:51)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Installing Sublime Text

On Ubuntu-based systems, you can install Sublime Text through the Ubuntu Software Center. Click the Ubuntu Software icon in your menu, and search for **Sublime Text**. Click to install it.

## Configuring Sublime Text

If you use the command **python** to launch a Python 3.6 or 3.7 session, Sublime Text should work by default. But if you use a command like **python3** or **python3.7**, you'll need to tell Sublime Text to use this command as well.

Open Sublime Text, and go to **Tools > Build System > New Build System**. This will open a new configuration file. Delete what you see, and enter the following:

```
{
    "cmd": ["python3", "-u", "$file"],
}
```

Save this file in the default location that Sublime Text suggests, with the name *Python3.sublime-build*. If you use the command **python3.7**, you should use that in the command shown here and save your file as *Python3.7.sublime-build*.

## Running programs with Sublime Text

If the command **python** works on your system and you haven't modified the build system as described above, you can click **Tools > Build**, or press Ctrl-B to run Python programs such as *hello_world.py*.

If you made a new build system, click **Tools > Build System** and click the build system you created, such as Python3 or Python3.7. After you've done this once, you can then just click **Tools > Build** or press Ctrl-B to run any Python program.