---
layout: default
title: Deployment is Complicated
parent: Deploying Django Projects
nav_order: 100
---

# Deployment is Complicated

The deployment process can be simplified, but even in simplified workflows there's a lot going on just out of sight. As soon as something doesn't go right, there's a bunch of complexity you might have to deal with.

## The simple, high-level view

From a high-level view, the deployment process is fairly simple:
- Make sure your project works on your local system.
- Copy your project to a remote server.
- Share the URL for your project with others.

## The reality

However, there are a number of factors that make deployment more complicated than that:

- Your OS is probably different than the server's OS.
- The server's resources are almost certainly much more limited than your local system.
- The load on the server can be much higher than the load on your local system, if people start using your site.
- The internet is a hostile place! Bots are constantly attacking deployed projects, even tiny test projects.
- People are constantly trying to abuse hosting platforms' free and intro offerings.

That last point is one of the main reasons the hosting landscape is changing so rapidly. Years ago, hosts could offer generous free plans that let you try out the deployment process, often without submitting credit card info. These days, any hosting service that lets you sign up without a credit card is inviting massive spamming attempts from crypto farmers and spammers, and many other fraudulent users.