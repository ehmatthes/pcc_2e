---
layout: default
title: Installing the Platform.sh CLI on Windows
parent: Deploying Django Projects
nav_order: 110
---

# Installing the Platform.sh CLI on Windows

One of the most significant difficulties in deploying from Windows is that the core Windows operating system is not the same as what a Linux-based remote server uses. A base Windows system has a different set of tools and languages than a base Linux system, so to carry out deployment work from Windows, you’ll need to choose how to integrate Linux-based tool sets into your local environment.

## Windows Subsystem for Linux

One popular approach is to use Windows Subsystem for Linux (WSL), an environment that allows Linux to run directly on Windows. If you have WSL set up, using the Platform.sh CLI on Windows becomes as easy as using it on Linux. The CLI won’t know it’s running on Windows; it will just see the Linux environment you’re using it in.

Setting up WSL is a two-step process: you first install WSL, and then choose a Linux distribution to install into the WSL environment. Setting up a WSL environment is more than can be described here; if you’re interested in this approach and don’t already have it set up, see the [WSL documentation](https://docs.microsoft.com/en-us/windows/wsl/about). Once you have WSL set up, you can follow the instructions in the instructions on the [Platform.sh CLI documentation](https://docs.platform.sh/administration/cli.html) page.

## Git Bash

Another approach to building a local environment that you can deploy from uses Git Bash, a terminal environment that’s compatible with Bash but runs on Windows. Git Bash is installed along with Git when you use the installer from https://git-scm.com. This approach can work, but it isn’t as streamlined as WSL. In this approach, you’ll have to use a Windows terminal for some steps and a Git Bash terminal for others.

First you’ll need to install PHP. You can do this with XAMPP, a package that bundles PHP with a few other developer-focused tools. Go to [https://apachefriends.org](https://apachefriends.org) and click the button to download XAMPP for Windows. Open the installer and run it; if you see a warning about User Account Control (UAC) restrictions, click OK. Accept all of the installer’s defaults.

When the installer finishes running, you’ll need to add PHP to your system’s path; this will tell Windows where to look when you want to run PHP. In the Start menu, enter **path** and click **Edit the System Environment Variables**; click the button labeled **Environment Variables**. You should see the variable `Path` highlighted; click **Edit** under this pane. Click **New** to add a new path to the current list of paths. Assuming you kept the default settings when running the XAMPP installer, add **C:\xampp\php** in the box that appears, then click **OK**. When you’re finished, close all of the system dialogs that are still open.

With these requirements taken care of, you can install the Platform.sh CLI. You’ll need to use a Windows terminal with administrator privileges; enter **command** into the Start menu, and under the Command Prompt app, click **Run as administrator**. In the terminal that appears, enter the following command:

<pre class="highlight"><code>> <b>curl -fsS https://platform.sh/cli/installer | php</b></code></pre>

This will install the Platform.sh CLI, as described earlier.

Finally, you’ll work in Git Bash. To open a Git Bash terminal, go to the Start menu and search for **git bash**. Click the **Git Bash app** that appears; you should see a terminal window open. You can use traditional Linux-based commands like `ls` in this terminal, as well as Windows-based commands like `dir`. To make sure the installation was successful, issue the **platform list** command. You should see a list of all the commands in the Platform.sh CLI. From this point forward, carry out all of your deployment work using the Platform.sh CLI inside a Git Bash terminal window.