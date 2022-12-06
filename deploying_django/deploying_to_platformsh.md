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

```
(ll_env)learning_log$ pip install platformshconfig
```

### Create a *requirements.txt* file

Generate a *requirements.txt* file with the following command:

```
(ll_env)learning_log$ pip freeze > requirements.txt
```

This looks at all the packages that have been installed to support the Learning Log project, and makes sure Platform.sh will install the same versions of those packages on its servers. You can open this file and see exactly which versions will be installed:

```
FILL
```

These are the most up to date versions at the time of this writing. If you see different versions in your output, you should keep those versions.

### Add `gunicorn` and `psycopg2`

The remote server will require two additional packages, that you don't need to install locally. Make a new file called *requirements_remote.txt*, and add the following two packages to it:

```
# Requirements for live projectt.
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

```
(ll_env)learning_log$ git --version
git version 2.30.1
```

If you need to install Git on Windows or macOS, go to [Git's website](https://git-scm.com) to download an installer. On apt-based Linux systems, the command `sudo apt install git-all` should work.

#### Configuring Git

If this is the first time you're using Git, you'll need to set your username and email:

```
(ll_env)learning_log$ git config --global user.name "username"
(ll_env)learning_log$ git config --global user.email "username@example.com"
```

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