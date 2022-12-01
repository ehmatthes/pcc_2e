---
layout: default
title: Deploying to Heroku
parent: Deploying Django Projects
nav_order: 10
---

# Deploying to Heroku

You can still deploy to Heroku, using the same process that's described in the book. There are some things you should know about Heroku's pricing plans, and it may be easier to follow the deployment steps here than going back to the book for the rest of the deployment process here.

* 
{:toc}

---

## Creating an account

Because Heroku no longer offers any free services, you'll need to have a credit card on file in order to create an account. There are no ways to set limits on the costs that you incur, so make sure you understand their pricing model, and how to monitor the charges that you're incurring.

When dealing with hosting services, you are entirely responsible for your bill. Platforms sometimes change their plans with no notice, so the only document that really matters is your invoice. You should verify everything you see here and anywhere else online against what you see in your Heroku dashboard. This is not unique to Heroku; this applies to any hosting service that you sign up for. It's also possible to create resources that are much more expensive than you intend, and only find out after you've incurred significant charges.

## Heroku's pricing model

Heroku uses "dynos" and "add-ons". You can think of a dyno as an app, and an add-on as a service. In the context of the Learning Log project, the dyno will handle the Django code, and an add-on will take care of the database.

Most of the pricing information you see summarized here is coming from Heroku's [Pricing](https://www.heroku.com/pricing) page.

### Basic dynos

This is where Heroku's pricing model is most complicated. If you don't specify a dyno type, Heroku will provision a Basic dyno.
- A Basic dyno costs \~$0.01 per hour, to a maximum of $7 per month.
- Basic dyno costs are prorated to the second.
- Basic dynos never sleep.

This is a common pricing approach for hosting platforms. "Prorated to the second", at about $0.01 per hour, means you can run a dyno for about $0.25 a day, or less than $2 a week.

### Eco dynos

You can specify an *Eco* dyno instead. Heroku's Eco offering is really a class of dynos.
- Eco dynos are a flat rate of $5/month.
- You get 1000 hours of usage across all of your Eco dynos. If you exceed this, all of your Eco dynos sleep until the start of the next billing cycle.
- There is no way to buy more Eco hours.If you need any of your apps to keep running, you would have to convert them to Basic dynos (or a higher level dyno).

This offering is Heroku's way to support people who want to deploy a number of small lightly-used projects, without racking up a $5/month per project bill. These are new, and it will be interesting to see how people start to use them.

### Choosing between Basic and Eco dynos

If you want to deploy a number of test projects and keep them running for a while, a set of Eco dynos seems like a good choice. You know you won't exceed $5/month for all the dynos, although you should understand how your databases will impact your overall cost.

If you want to deploy a test project with the intention of destroying it in a short time, anywhere from a day to two weeks, a Basic dyno may be the best choice. You'll get the advantage of prorated costs.


### Database pricing

Most Django projects require a database. When you push to Heroku with the default deployment configuration, a Postgres database add-on will be created for your project. Databases come in any number of configurations; the default configuration is called a [Mini](https://elements.heroku.com/addons/heroku-postgresql), and it costs just under $0.01/hour, with a maximum of $5/month.

This is per-project, however. So you can use a number of Eco dynos to deploy a few small projects, but each project will require a separate database under the default configuration.

### Monitoring your costs

## Deploying Learning Log