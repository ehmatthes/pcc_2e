---
layout: default
title: Deploying Django Projects
has_children: true
nav_order: 55
has_toc: false
---

# Deploying Django Projects
{: .no_toc }

Building a Django project that works on your system is satisfying, but it gets even more satisfying when you see your site deployed where anyone can access it. The deployment process changes rapidly, so these resources may be more up to date than what you see in your copy of the book.
{: .fs-6 .fw-300 }

## Changes at Heroku

Heroku was the first hosting platform to offer a really simple deployment process. With proper configuration, they made it so you can deploy your project with one command: `git push heroku main`. When Heroku started they let you sign up without a credit card, and you could deploy up to 5 projects at any one time using their free plan. Projects would sleep when not in use, but that was quite reasonable for a free offering, and it let thousands of people learn about deployment.

Because free plans incur [lots of abuse](deployment_is_complicated), Heroku just closed out their free tier.

## Deploying Learning Log

The only inaccurate part of the deployment section of Chapter 20 is the statement that Heroku offers a free tier. You can still deploy to Heroku, but there are some things you should know about their pricing plans before doing so. You may want to try a different platform that still offers a free tier.

### Deploying to Heroku

If you are willing to pay for hosting, you can still deploy to Heroku. Pricing for most plans is pro-rated to the second, so deploying a project and then destroying it can cost very little. The cheapest ongoing deployment is about $10-$12 month.

[Deploy to Heroku](deploying_to_heroku)

### Deploying to Platform.sh

The third edition of Python Crash Course walks through deployment to Platform.sh, which as of this writing does not require a credit card. If you'd rather deploy to Platform.sh, you can follow the instructions here:

[Deploy to Platform.sh](deploying_to_platformsh)