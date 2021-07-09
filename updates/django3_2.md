---
layout: default
title: Django 3.2
parent: Updates
nav_order: 1010
---

# Django 3.2
{: .no_toc }

* 
{:toc}

Back to [Updates](../updates/)

---

## Overview

Django 3.2 was released in April 2021. Everything in the Learning Log project (Chapters 18-20) should still work as it's written with only minor changes. For these updates, see the section [Deploying to Heroku](#deploying-to-heroku) at the end of this page.

The core parts of Django are really stable; there is nothing in the new release that affects the Learning Log project. All of the [new features](https://docs.djangoproject.com/en/3.2/releases/3.2/) are for more advanced use cases, and help keep the framework running efficiently.

[top](#top)

## The Django Release Cycle

If you're interested in building real-world Django projects, it's important to understand the Django release cycle. Every site on the internet is open to attack. These days you don't have to be an attractive target to be attacked; bots are constantly attacking random sites to try and find a way into various hosting platforms and server networks. Django, and every other decent web framework, is updated on a regular basis to support new features, deprecate outdated features, and remain relatively safe from new and ongoing attacks.

Each Django release has a major version number, a minor number, and a patch number. Django recently went from version 2.2.8 to version 3.0.0. This was nothing like the transition from Python 2 to Python 3; there were few if any breaking changes when upgrading a Django 2.2 project to run on Django 3.0.

Django releases are supported for about 16 months. Some releases, designated *LTS* for *Long Term Support*, are supported for about 3 years. Django 3.2 is the most recent LTS release. Here's a great [visual representation](https://www.djangoproject.com/download/#supported-versions) and description of the official release cycle.

If you want to see a detailed description of the Django release process, you can find the [documentation here](https://docs.djangoproject.com/en/3.2/internals/release-process/). If you want to see the entire evolution of Django, all of the release notes to date are [listed here](https://docs.djangoproject.com/en/dev/releases/).

[top](#top)

## Should I upgrade?

That depends on what you're working on:

### Starting a New Django Project with Django 3.2

If you're starting a brand new Django project, Django 3.2 will be installed for you automatically, and you should use this.

### Upgrading an Existing Project to Django 3.2

If you're already working on a Django project, you don't need to upgrade if your version is still being supported. But if you want to use the latest version, here's how to do it. I'll describe this in the context of upgrading a Learning Log project that's currently running on Django 3.1.

- Close all terminals where the virtual environment is active. (This isn't absolutely necessary, but it's certainly a good idea if you've got a number of terminals open.)
- Open a terminal, and activate the virtual environment.
- Run the following command:

    `(ll_env) learning_log$ pip install --upgrade django`

  - This command will uninstall any version of Django that's already installed in the active virtual environment, and install the latest version of Django.
- Continue working on the project.
  - It's a good idea to start the development server, and make sure everything that was working still works.
  - If you were using this process to upgrade to a version with some breaking changes, you'd look at the problematic functionality and update your code to use Django's current features in your project.
- If you're upgrading Learning Log from an earlier version to 3.2, make sure you see the section about [deploying to Heroku](#deploying-to-heroku) below.

[top](#top)

## Deploying to Heroku

There are two minor changes you may need to make in order to deploy your Learning Log project to Heroku.

### The `psycopg2` package

On page 448 in the section *Installing Required Packages*, it says to install the package `psycopg2==2.7.*`. This should be changed to `psycopg2-binary` if you're seeing errors related to the psycopg2 package during the deployment process.

### The Python Runtime

The latest Python runtimes available on Heroku are listed [here](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version). The ones you're probably interested in are `python-3.9.6` and `python-3.8.11`. You can use either of these in the *runtime.txt* file described on page 449.

This is not a critical update; if you specify a runtime that's slightly out of date, Heroku will use the closest match it finds in its available runtimes.
