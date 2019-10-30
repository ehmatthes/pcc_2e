---
layout: default
title: Setting up Python on macOS
parent: Setup Instructions
nav_order: 2
---

# Setting up Python on macOS
{: .no_toc }

* 
{:toc}

---

## Checking your current version of Python

Python is installed by default on macOS, but it's often a very old version of the language. To see if you have a recent version installed, issue the following command:

```bash
$ python3 --version
Python 3.8.0
```

If you see something like this, you already have Python installed. You'll need Python 3.6 or higher to follow along with the book. If you see a version earlier than Python 3.6, or if you see an error message, it's fairly straightforward to install a newer version of Python.

## Installing Python 3.8

Go to [https://python.org/](https://python.org), and hover over the **Download** link. You should see a button for downloading the latest version of Python. Click the link, and run the installer.

When you're finished, open a new terminal window and run the **python3** command again:

```bash
$ python3
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

To exit the Python session, press **Ctrl-D** or enter the command **exit()**.

## Installing Sublime Text

To install Sublime Text, go to [https://sublimetext.com/](https://sublimetext.com). Click the **Download** link and look for a macOS installer. Run the installer and drag the Sublime Text icon into your Applications folder.

## Configuring Sublime Text

If you use the command **python** to launch a Python 3.6, 3.7, or 3.8 session, Sublime Text should work by default. But if you use a command like **python3** you'll need to tell Sublime Text to use this command as well.

Open Sublime Text, and go to **Tools > Build System > New Build System**. This will open a new configuration file. Delete what you see, and enter the following:

```
{
    "cmd": ["python3", "-u", "$file"],
}
```

Save this file in the default location that Sublime Text suggests, with the name *Python3.sublime-build*.

## Running programs with Sublime Text

If the command **python** works on your system and you haven't modified the build system as described above, you can click **Tools > Build**, or press Ctrl-B to run Python programs such as *hello_world.py*.

If you made a new build system, click **Tools > Build System** and click the build system you created, which should be Python3. After you've done this once, you can then just click **Tools > Build** or press Command-B to run any Python program.

## Troubleshooting

If that didn't work for some reason, [click here for some troubleshooting help](../troubleshooting_macos/).