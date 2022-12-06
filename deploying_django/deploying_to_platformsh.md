---
layout: default
title: Deploying to Platform.sh
parent: Deploying Django Projects
nav_order: 20
---

# Deploying to Platform.sh
{: .no_toc }

The third edition of Python Crash Course walks readers through the process of deploying the Learning Log project to [Platform.sh](https://platform.sh), a hosting site that still offers a free trial. As of this writing, the free trial lasts for 30 days and does not require a credit card when you sign up. You are limited to two apps in a 24-hour period while on the free trial. 

The description of the deployment process shown here is not as thorough as what you'd find in the third edition, but should be clear enough to make a successful deployment if you've finished the Learning Log project through the first half of Chapter 20 in the second edition.

* 
{:toc}

---

## Deploying Learning Log

### Make a Platform.sh account

Go to the [Platform.sh](https://platform.sh) home page and make an account.

When dealing with hosting services, you are entirely responsible for your bill. Platforms sometimes change their plans with no notice, so the only document that really matters is your invoice. You should verify everything you see here and anywhere else online against what you see in your Platform.sh dashboard. This is not unique to Platform.sh; this applies to any hosting service that you sign up for. It’s also possible to create resources that are much more expensive than you intend, and only find out after you’ve incurred significant charges. Keep this in mind if you keep your account active long enough to put a credit card on file.

### Install the Platform.sh CLI

Visit [The Platform.sh CLI](https://docs.platform.sh/administration/cli.html) documentation page for instructions about how to install the Platform.sh CLI on your system.

**Note:** On Windows, you'll need to use the Windows Subsystem for Linux (WSL) a Git Bash terminal, or another Bash-compatible terminal. See [add external page]().

### Install `platformshconfig`

The `platformshconfig` package helps detect whether the project is running on your local system, or on a Platform.sh server. It also handles some configuration work on the remote server. Use `pip` to install it:

<pre class="highlight"><code>(ll_env)learning_log$ <b>pip install platformshconfig</b></code></pre>

### Create a *requirements.txt* file

Generate a *requirements.txt* file with the following command:

<pre class="highlight"><code>(ll_env)learning_log$ <b>pip freeze > requirements.txt</b></code></pre>

This looks at all the packages that have been installed to support the Learning Log project, and makes sure Platform.sh will install the same versions of those packages on its servers. You can open this file and see exactly which versions will be installed:

```
FILL
```

These are the most up to date versions at the time of this writing. If you see different versions in your output, you should keep those versions.

### Add `gunicorn` and `psycopg2`

The remote server will require two additional packages, that you don't need to install locally. Make a new file called *requirements_remote.txt*, and add the following two packages to it:

```
# Requirements for live project.
gunicorn
psycopg2
```

The `gunicorn` package handles live requests just like `runserver` does locally, but it can handle multiple simultaneous requests. The `pscyopg2` package helps Django manage the Postgres database that Platform.sh uses.

### Add configuration files

Platform.sh deployments need two configuration files:

- ***.platform.app.yaml*** This is the main configuration file for the project.
- ***.platform/services.yaml*** THis file defines additional services the project needs.

The first is a single file that needs to start with a dot. The second is a file called *services.yaml*, in a folder called *.platform*. Files and folders that start with a dot are called *dotfiles*, or *hidden files*, because they're often hidden by file browsers.

#### Making hidden files visible

You may need to make some changes to see hidden files and folders on your system:

- On Windows, open Windows Explorer, and then open a folder such as *Desktop*. Click the **View** tab, and make sure **File name extensions** and **Hidden items** are checked.
- On macOS, you can press `Cmd-Shift-.` in any file browser window to see hidden files and folders.
- On Linux systems such as Ubuntu, you can press `Ctrl-H` in any file browser to display hidden files and folders. To make this setting permanent, open a file browser such as Nautilus and click the options tab (indicated by three lines). Select the **Show Hidden Files** checkbox.

#### The *.platform.app.yaml* file

This is the longer configuration file, because it controls the overall deployment process. Open a new window in an editor, paste the following into it, and save it as *.platform.app.yaml*:

```yaml
name: "ll_project"
type: "python:3.10"

relationships:
    database: "db:postgresql"

# The configuration of the app when it's exposed to the web.
web:
    upstream:
        socket_family: unix
    commands:
        start: "gunicorn -w 4 -b unix:$SOCKET ll_project.wsgi:application"
    locations:
        "/":
            passthru: true
        "/static":
            root: "static"
            expires: 1h
            allow: true

# The size of the persistent disk of the application (in MB).
disk: 512

# Set a local read/write mount for logs.
mounts:
    "logs":
        source: local
        source_path: logs

# The hooks executed at various points in the lifecycle of the application.
hooks:
    build: |
        pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements_remote.txt
        
        mkdir logs
        python manage.py collectstatic
        rm -rf logs
    deploy: |
        python manage.py migrate
```

You don't need to understand everything here, but you should skim it and get an idea of what it's doing for you. It specifies the name of the project, and the version of Python we're using. The Platform.sh documentation has a list of [currently supported Python versions](https://docs.platform.sh/languages/python.html).

The `relationships` section defines other services the project needs, in this case a database. The `web` section tells the server how to respond to incoming requests for specific pages, and resources needed to build pages.

We're requesting 512MB of disk space, and we're setting up a place for log files. Finally, in the `hooks` section, we tell the server which packages to install (from the *requirements.txt* and *requirements_remote.txt* files). We also run the `migrate` command during the deployment process.

#### The *.platform/services.yaml* file

Make a new folder called *.platform*, in the same directory as *manage.py*. Make sure you include the dot at the beginning of the name. Inside that folder, make a file called *services.yaml* and enter (or paste) the following:

```yaml
# Each service listed will be deployed in its own container as part of your
#   Platform.sh project.

db:
    type: postgresql:12
    disk: 1024
```

This file defines one service, a Postgres database.

### Modify *settings.py* for Platform.sh

Copy and paste the following section into the end of *settings.py*:

```python
--snip--

# Platform.sh settings.
from platformshconfig import Config

config = Config()
if config.is_valid_platform():
    ALLOWED_HOSTS.append('.platformsh.site')
    DEBUG = False

    if config.appDir:
        STATIC_ROOT = Path(config.appDir) / 'static'
    if config.projectEntropy:
        SECRET_KEY = config.projectEntropy

    if not config.in_build():
        db_settings = config.credentials('database')
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': db_settings['path'],
                'USER': db_settings['username'],
                'PASSWORD': db_settings['password'],
                'HOST': db_settings['host'],
                'PORT': db_settings['port'],
    },
}
```

This imports the `platformshconfig` package, and then makes configuration changes that are specific to the deployed version of the project. It allows the project to be served by hosts ending in *.platformsh.site*, handles static files correctly, and configures the `SECRET_KEY` and `DATABASE` settings.

### Use Git to track the project

Git is a source code management tool. Git is used for almost all deployment workflows, because you can make "snapshots" of your projects called *commits*. If your deployment stops working, you can use Git to revert back to the last working commit of your project, and avoid significant downtime in your projects.

#### Installing Git

Check if Git is already installed on your system:

<pre class="highlight"><code>(ll_env)learning_log$ <b>git --version</b>
git version 2.30.1</code></pre>

If you need to install Git on Windows or macOS, go to [Git's website](https://git-scm.com) to download an installer. On apt-based Linux systems, the command `sudo apt install git-all` should work.

#### Configuring Git

If this is the first time you're using Git, you'll need to set your username and email:

<pre class="highlight"><code>(ll_env)learning_log$ <b>git config --global user.name "username"</b>
(ll_env)learning_log$ <b>git config --global user.email "username@example.com"</b></code></pre>

You can use your actual email address, or an address ending in example.com.

#### Make a *.gitignore* file

Git shouldn't track every file in the project, so we'll write a *.gitignore* file telling Git which files it doesn't need to track:

```
ll_env/
__pycache__/
*.sqlite3
```

We don't want to push the virtual environment, Python's cached files, or the local database. If you're on macOS, you can add `.DS_Store` to this file as well.

Make sure you save this file with a dot in front of it; it needs to be called `.gitignore`, not `gitignore`. It also can't have a file ending such as `.txt`.

### Creating a project on Platform.sh

The Learning Log project still runs locally, and is now configured for deployment to Platform.sh as well. Log in to the Platform.sh CLI in the terminal:

<pre class="highlight"><code>(ll_env)learning_log$ <b>platform login</b>
Opened URL: http://127.0.0.1:5000
Please use the browser to log in.
--snip--
Do you want to create an SSH configuration file automatically? [Y/n] <b>Y</b>
</code></pre>

A browser tab will open where you can log in. Once you're logged in you can close the browser tab. If you're prompted about creating an *SSH configuration file*, enter **Y** so you can connect to the remote server later.

Now you can create a project. There are a few prompts that will come up. Start by issuing the `platform create` command:

<pre class="highlight"><code>(ll_env)learning_log$ <b>platform create</b>
* Project title (--title)
Default: Untitled Project
> <b>ll_project</b>

* Region (--region)
The region where the project will be hosted
  --snip--
  [us-3.platform.sh] Moses Lake, United States (AZURE) [514 gC02eq/kWh]
> <b>us-3.platform.sh</b>
* Plan (--plan)
Default: development
Enter a number to choose:
  [0] development
  --snip--
> <b>0</b>

  * Environments (--environments)
  The number of environments
  Default: 3
> <b>3</b>

  * Storage (--storage)
  The amount of storage per environment, in GiB
  Default: 5
> <b>5</b>

Default branch (--default-branch)
The default Git branch name for the project (the production environment)
Default: main
> <b>main</b>

Git repository detected: /Users/eric/.../learning_log
Set the new project ll_project as the remote for this repository? [Y/n] <b>Y</b>

The estimated monthly cost of this project is: $10 USD
Are you sure you want to continue? [Y/n] <b>Y</b>

The Platform.sh Bot is activating your project
  ▀▄   ▄▀  
█▄█▀███▀█▄█
▀█████████▀
 ▄▀     ▀▄ 
           
  The project is now ready!</code></pre>

You'll be prompted for a name to use for the deployed project, which is `ll_project` in the output shown here. Then you'll be prompted to choose a region near you; for me that's `us-3.platform.sh`. You'll be prompted to choose a plan type, the number of environments, a storage amount, and the main branch name. The default options should work for all of these. You'll need to answer **Y** to set the remote repository, and confirm what the cost of the plan would be if you continue to use it beyond the free tier.

You'll see a dancing robot while your project is activated.

### Pushing the project

The last step before seeing the live version of the project is to push your code to the remote server, using the `platform push` command:

<pre class="highlight"><code>(ll_env)learning_log$ <b>platform push</b>
Are you sure you want to push to the main (production) branch? [Y/n] <b>Y</b>
--snip--
The authenticity of host 'git.us-3.platform.sh (...)' can't be established.
RSA key fingerprint is SHA256:Tvn...7PM
Are you sure you want to continue connecting (yes/no/[fingerprint])? <b>Y</b>
Pushing HEAD to the existing environment main
  --snip--
  To git.us-3.platform.sh:3pp3mqcexhlvy.git
   * [new branch]      HEAD -> main</code></pre>

You'll be asked for one more confirmation that you actually want to push the project. You might see a message about confirming th authenticity of Platform.sh as well.

After these final prompts, you should see a bunch of output scroll by as your code is copied to the server, and the project is built out on the remote server.

**Note:** If realize you made a mistake such as a typo in a configuration file, fix the mistake and then reissue the `git commit` command. Then you can run `platform push` again. You shouldn't need to repeat the `platform create` command, as that would just make an additional project on your Platform.sh account.

### Viewing the project

You can see your project using the `platform url` command:

<pre class="highlight"><code>(ll_env)learning_log$ <b>platform url</b>
Enter a number to open a URL
  [0] https://main-bvxea6i-wmye2fx7wwqgu.us-3.platformsh.site/
  --snip--
> <b>0</b></code></pre>

The `platform url` command lists the URLs associated with a deployed project. Choose one, and your project should open in a new browser tab.

**Note:** When you deploy your project using a trial account, don’t be surprised if it sometimes takes longer than usual for a page to load. On most hosting platforms, free resources that are idle are often suspended and only restarted when new requests come in. Most platforms are much more responsive on paid hosting plans.

### Creating a superuser

The database for the live project has been set up, but it's completely empty. To create a superuser on the deployed project, we'll start an SSH session where we can run management commands on the remote server:

<pre class="highlight"><code>(ll_env)learning_log$ <b>platform environment:ssh</b>

   ___ _      _    __                    _
  | _ \ |__ _| |_ / _|___ _ _ _ __    __| |_
  |  _/ / _` |  _|  _/ _ \ '_| '  \ _(_-< ' \
  |_| |_\__,_|\__|_| \___/_| |_|_|_(_)__/_||_|

   Welcome to Platform.sh.

web@ll_project.0:~$ <b>ls</b>
users learning_logs ll_project logs manage.py requirements.txt
    requirements_remote.txt static
web@ll_project.0:~$ <b>python manage.py createsuperuser</b>
Username (leave blank to use 'web'): <b>ll_admin_live</b>
Email address:
Password:
Password (again):
Superuser created successfully.
web@ll_project.0:~$ <b>exit</b>
logout
Connection to ssh.us-3.platform.sh closed.
(ll_env)learning_log$</code></pre>

When you first run the command `platform environment:ssh`, you may get another prompt about the authenticity of this host. If you see this, enter `Y` and you should be logged into a remote terminal session.

After running the `ssh` command, your terminal acts just like a terminal on the remote server. Your prompt will change to indicate that you're in a *web* session associated with the project named *ll_project*. Issuing the `ls` command will list the files that were pushed to the remote server.

Issue the same `createsuperuser` command you used in Chapter 18. This time I used the name `ll_admin_live`, so I have a separate username that's clearly associated with the deployed project. When you're finished, enter `exit` to end the SSH session. You'll see from the prompt that you're back in your local system.

**Note:** Windows users will use the same commands shown here (such as `ls` instead of `dir`), because you’re running a Linux terminal through a remote connection.

### Securing the project

