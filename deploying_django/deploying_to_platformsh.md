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

