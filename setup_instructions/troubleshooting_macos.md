---
layout: default
---

# Troubleshooting macOS Installations
{: .no_toc }

* 
{:toc}

---

The most common issue when setting up your system is configuring Sublime Text to run your programs. To run your programs, Sublime Text needs to know what command to use when running Python programs on your computer.

## Starting a Python Terminal Session

If you can start a Python terminal session, you'll know the command to use when configuring Sublime Text. On most macOS systems, the command **python** points to an older, outdated version of Python that is just used for system-level programs:

```
$ python --version
Python 2.7.15
```

If you used the offical Python installer from [python.org](https://python.org/), then **python3** probably points to the version of Python you want Sublime Text to use:

```
$ python3 --version
Python 3.8.0
```

For the rest of this guide, we'll assume that the command **python3** works on your system.

## Verifying Your Sublime Text Configuration

When you run a Python program, Sublime Text tells the Python interpreter to run your program, and Sublime Text then shows you the results. When you first install Sublime Text, it's configured to run any file ending in *.py* using the command **python**.

If you're at this troubleshooting page, you probably already defined a build system using the **New Build System** command (see *Configuring Sublime Text* [here](../macos/#configuring-sublime-text)). Hopefully you saved that file in the default location that Sublime Text suggests, and called it *Python3.sublime-build*. If you didn't do that, go back and try it.

If things are still not working, you'll need to open that file.

- Open your *hello_world.py* file in Sublime Text, so you have a Python file open.
- Go to **Sublime Text > Preferences > User**.
- Expand the *User* folder that appears, and you should see your *Python3.sublime-build* file listed. Double click the file to open it. If you don't see this file, then your build system was probably not saved. Try the **New Build System** command again, as described in the *Configuring Sublime Text* section [here](../macos/#configuring-sublime-text), and see if you get different results.

You should see something like the following:

```
{
    "cmd": ["python3", "-u", "$file"],
}
```

To troubleshoot this, it's helpful to know a bit more about how this file works. The line above tells Sublime Text to run a Python program by using the **python3** command with the **-u** flag, on the file that's currently open. That command, for *hello_world.py*, would look like this:

```
$ python3 -u hello_world.py
```

The -u flag helps Sublime Text display the output properly in its own embedded terminal window.

If your *Python3.sublime-build* file looks correct, try running *hello_world.py*. Click the window where *hello.py* is open, go to **Tools > Build System**, and click **Python3**. Then go to **Tools > Build**, or press **Cmd-B**. You should see *Hello Python world!* in an output window at the bottom of the Sublime Text window. If you see this, you're all set!

If you don't see any results, or if you see an error, you can try running your program in a terminal.

# Running *hello_world.py* from a terminal

Running *hello_world.py* from a terminal will tell you whether you're using the correct command to configure Sublime Text.

- Open a terminal window. To do this, press **Cmd-Space**, enter *terminal*, and press **Enter**.
- You'll see a prompt, probably at your home folder (**~$**). If you're new to using a terminal, there are two commands that will help you right away.
    - The command **ls** (lowercase LS) will *list* the folders and files in the directory you're currently in.
    - The command **cd *foldername*** will move you into any folder inside the current directory.
    - The command **cd ..** will move you up one level from the current directory.
  - With some practice, these three commands will let you move through your filesystem just like you typically do in a Finder window.
- Navigate to your *python_work* folder, or the folder where you saved *hello_world.py*.
- Issue the command `python3 hello_world.py`. You should see the output *Hello Python world!*
  - If this command doesn't work, then something happened when you installed Python 3. It may not be installed properly, or it may have been set up with a command other than **python3**.
  - If this command works in the terminal, then something is wrong with your Sublime Text configuration.

If you made a *python_work* folder on your Desktop, the above steps would look something like this:

```
~$ ls
Applications
Desktop
Documents
--snip--
~$ cd Desktop
~/Desktop$ ls
python_work
pcc_work
--snip--
~/Desktop$ cd python_work
~/Desktop/python_work$ ls
hello_world.py
~/Desktop/python_work$ python3 hello_world.py
Hello Python world!
```

# If you're still stuck...

If you're still stuck, first of all I'm sorry you're having difficulty. Sometimes getting your system set up properly is harder than learning to write code. There are lots of things that can go wrong, and they can be quite difficult to diagnose if you haven't explored the internal workings of a computer before.

If you've tried the steps in this guide and things still aren't working, please let me know. I like to know that everyone who's interested in learning to program can at least get started on the journey. If your issue points to something that I should clarify in this guide, I'll add that in and it will help others. If your issue is more subtle or unique, then you'll know it wasn't anything on your part that caused the issue.

To get in touch, please send an email with the following information:
- What OS are you using, and what version of the OS do you have installed?
- How did you install Python?
- What steps have you taken to configure your system?
- What results are you getting? (Are you getting a specific error, or are you just gettting no results at all?)

I can be reached at ehmatthes at gmail. Thank you!









