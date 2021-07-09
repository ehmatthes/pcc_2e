---
layout: default
title: Django 3.0
---

# Django 3.0
{: .no_toc }

* 
{:toc}

Back to [Updates](../updates/)

---

## Overview

Django 3.0 was released on December 2, 2019. Everything in the Learning Log project (Chapters 18-20) should still work as it's written with one minor change. For that update, see the section [Deploying to Heroku](#deploying-to-heroku) at the end of this page.

The core parts of Django are really stable; there is nothing in the new release that affects the Learning Log project. All of the [new features](https://docs.djangoproject.com/en/3.0/releases/3.0/) are for more advanced use cases, and many of the changes are laying the groundwork that will allow asynchronous functionality in future versions of Django.

You might want to know some more about new releases in Django. Here's a brief summary, including some links to the official documentation. If you plan to continue working with Django, it's important to know what to look for when new releases come out.

[top](#top)

## The Django Release Cycle

If you're interested in building real-world Django projects, it's important to understand the Django release cycle. Every site on the internet is open to attack. These days you don't have to be an attractive target to be attacked; bots are constantly attacking random sites to try and find a way into various hosting platforms and server networks. Django, and every other decent web framework, is updated on a regular basis to support new features, deprecate outdated features, and remain relatively safe from new and ongoing attacks.

Each Django release has a major version number, a minor number, and a patch number. Django just went from version 2.2.8 to version 3.0.0. This is nothing like the transition from Python 2 to Python 3; there are few if any breaking changes when upgrading a Django 2.2 project to run on Django 3.0.

Django releases are supported for about 16 months. Some releases, designated *LTS* for *Long Term Support*, are supported for about 3 years. Django 2.2 was the most recent LTS release. Here's a great [visual representation](https://www.djangoproject.com/download/#supported-versions) and description of the official release cycle.

If you want to see a detailed description of the Django release process, you can find the [documentation here](https://docs.djangoproject.com/en/3.0/internals/release-process/). If you want to see the entire evolution of Django, all of the release notes to date are [listed here](https://docs.djangoproject.com/en/3.0/releases/).

[top](#top)

## Should I upgrade?

That depends on what you're working on:

### Starting a New Django Project with Django 3.0

If you're starting a brand new Django project, Django 3.0 will be installed for you automatically, and you should probably use this.

### Starting a New Django Project using Django 2.2 LTS

If you're starting a real-world project and you want to use the latest LTS release, you can use the following command in a virtual environment:

    $ python -m pip install django==2.2

### Upgrading an Existing Project to Django 3.0

If you're already working on a Django project, you don't need to upgrade if your version is still being supported. But if you want to use the latest version, here's how to do it. I'll describe this in the context of upgrading a Learning Log project that's currently running on Django 2.2.

- Close all terminals where the virtual environment is active. (This isn't absolutely necessary, but it's certainly a good idea if you've got a number of terminals open.)
- Open a terminal, and active the virtual environment.
- Run the following command:

    `(ll_env) learning_log$ pip install --upgrade django`

  - This command will uninstall any version of Django that's already installed in the active virtual environment, and install the latest version of Django.
- Continue working on the project.
  - It's a good idea to start the development server, and make sure everything that was working still works.
  - If you were using this process to upgrade to a version with some breaking changes, you'd look at the problematic functionality and update your code to use Django's current features in your project.

[top](#top)

## Upgrading to Python 3.8

If you created your virtual environment with an earlier version of Python and recently upgraded to Python 3.8, you can rebuild the entire virtual environment to use your new version of Python:

- Close all terminals where the virtual environment is active.
- Delete the *ll_env* folder.
  - You won't lose anything specific to your project. That's the whole point of using a virtual environment; you can destroy and rebuild the environment anytime you need.
- Recreate the virtual environment using your new version of Python.
  - Run the `venv` command using your current Python command:

      `$ python -m venv ll_env`

  - For some people this might be `python3`, `py`, or `python3.8`.
- Activate the virtual environment.
- Install the latest version of Django:

    `(ll_env) learning_log$ pip install django`

- If you have used other libraries, install them as well.
  - If you've only installed them manually, you can reinstall them manually:

    `(ll_env) learning_log$ pip install django-bootstrap4`
  
  - If you have a *requirements.txt* file, you can install all of your requirements from that file:

    `(ll_env) learning_log$ pip install -r requirements.txt`
  
  - Keep in mind this will install the previously-specified version of these libraries. If you want to upgrade all of these libraries, you can delete the *requirements.txt* file and install each of the libraries you used by hand again. Then when they're all installed, rerun the `pip freeze > requirements.txt` file to create an updated set of requirements for the project.

[top](#top)

## Deploying to Heroku

### The `psycopg2` package

There's only one minor change you'll need to make in order to deploy your Learning Log project to Heroku. On page 448 in the section *Installing Required Packages*, it says to install the package `psycopg2==2.7.*`. This should be changed to `psycopg2-binary`.

### The Python Runtime

The latest Python runtimes available on Heroku are listed [here](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version). The ones you're probably interested in are `python-3.8.0` and `python-3.7.5`. You can use either of these in the *runtime.txt* file described on page 449.

This is not a critical update; if you specify a runtime that's slightly out of date, Heroku will use the closest match it finds in its available runtimes.
