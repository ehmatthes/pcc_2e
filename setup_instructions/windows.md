---
layout: default
title: Setting up Python on Windows
parent: Setup Instructions
nav_order: 1
---

# Setting up Python on Windows
{: .no_toc }

* 
{:toc}

---
## Checking your current version of Python

Python may already installed on your system. Open a command window by right-clicking on the Desktop while holding the Shift key, and then select “Open Command Window Here”. You can also search for “command” in the task bar. Find out which version is your default by issuing the command `python --version`:

```bash
> python --version
Python 3.7.2
```

If you see something like this, you already have Python installed. You'll need Python 3.6 or higher to follow along with the book. If you see a version earlier than Python 3.6, or if you see an error message, it's fairly straightforward to install a newer version of Python.

## Installing Python 3.7

Go to [https://python.org/](https://python.org/) and hover over the **Downloads** link. You should see a link for your operating system; click the link and download the appropriate installer for your system.

Run the installer, making sure to check the *Add Python to PATH* checkbox.

![](../../images/crash_course01-1.png)

To confirm that the installation was successful, open a terminal and start a Python session:

```bash
> python
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

To exit the Python session, press **Ctrl-Z** or enter the command **exit()**.

## Installing Sublime Text

You can download an installer for Sublime Text from [https://sublimetext.com](https://sublimetext.com). Click the link and look for a Windows installer. Download the installer and run it.

Assuming you use the command **python** to start a Python terminal session, Sublime Text should not require any configuration to run Python programs on your system.