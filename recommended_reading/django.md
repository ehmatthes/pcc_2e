---
layout: default
title: Django Resources
parent: Recommended Reading
nav_order: 40
---

# Django Resources
{: .no_toc }

*Note: This is a work in progress. I will be adding to this as I have time over the next week or so.*

Django has been one of the most prominent Python web frameworks for almost 15 years now. Django is downloaded about 200,000 times each day, and powers millions of websites. You can use it for small projects where you're the only user, or for projects that just serve the teams you work with. But it's also powerful enough to serve some of the most popular sites on the internet such as Instagram, Pinterest, and Disqus.

You can use books to get started with Django, but once you learn the overall structure of Django projects and how to do common tasks, you'll want to become familiar with the official documenation and some other online resources. Django has some of the best documentation of any open source project, and it's well worth your time to become familiar wtih it. This section will help you find some good followup resources after working through the Learning Log project, and also familiarize you with resources you're likely to use as long as you're an active Django developer.

Note: Some of the resources mentioned in the [General Python Resources](../general_python/) have sections that are relevant to Django developers. I won't repeat those resources here, but you should check them out as well.

* 
{:toc}

---

## The Official Django Tutorial (The Polls Tutorial)

The Django documentation includes an in-depth tutorial that's really worth going through. In fact, I highly recommend it as your next step after completing the Learning Log project. You'll be familiar wtih much of what you see, but you'll also learn more details about many aspects of Django, and see some new features as well. For example you'll see how to test your Django apps, which is absolutely critical for many webapp-based projects. The tutorial also has links to the technical documentation throughout, which is a great way to start exploring the technical documentation.

Almost everyone in the Django community has worked through the Polls tutorial at some point, and working through it gives you common ground in your early communication with other Django developers.

You can start with an [overview](https://docs.djangoproject.com/en/3.0/intro/) of all the parts of the tutorial, or you can straight to [part 1](https://docs.djangoproject.com/en/3.0/intro/tutorial01/). (When it tells you to install Django, it's a good idea to set up a virtual environment for the tutorial project just like we did in the Learning Log project. I would call it `pt_env`, for "polls tutorial environment." Also, when you've finished the tutorial you might try pushing the project to Heroku.)

[top](#top)

---

## Books and Print Resources

### Django for Beginners, Django for APIs, and Django for Professionals, by [Will Vincent](https://twitter.com/wsv3000)

I haven't read any of thse books, but I've read many of Will Vincent's articles about specific topics in Django. Every article has been accurate and up to date, with clear instructions and explanations. I have no doubt his books are of the same quality. Will is also a board member of the [Django Software Foundation](https://www.djangoproject.com/foundation/), and he co-hosts the [Django Chat] podcast and co-curates the weekly [Django News](https://django-news.com) newsletter.

*Django for Beginners* walks you through building a series of increasingly complex websites using Django. *Django for APIs* shows you how to build web apps where Django is used for the backend and a JavaScript library (React in this case) is used for the frontend. *Django for Professionals* takes you from the tutorial-focused world to the real world by building a professional-quality project complete with support for payments through Stripe.

If you're interested in any of these books, you can see more about them and buy them at [learndjango.com](https://learndjango.com). There's a discount if you buy the three books as a bundle.

![](../../images/recommended_reading/wvd_covers.png)

[top](#top)

### Django Crash Course, by [Daniel Feldroy](https://twitter.com/pydanny/) and [Audrey Feldroy](https://twitter.com/audreyr)

Daniel and Audrey Feldroy are the authors of *Two Scoops of Django*, which focuses on more advanced aspects of Django. *Django Crash Course* (which has no affiliation with *Python Crash Course*) is their foray into introductory Django topics. *Django Crash Course* is based on materials that Daniel and Audrey have used for years in corporate training programs. They have repackaged their material to be accessible to anyone already familiar with Python, but not necessarily having a background in Django. They are planning a series of extensions to the book which will cover specific topics that build on the material in this book.

*Django Crash Course* is available now as an ebook. You can preorder a paperback, coil-bound, or hardbound copy as well. All of these versions are available [here](https://www.feldroy.com/products/django-crash-course).

![](../../images/recommended_reading/dcc_cover.png)

[top](#top)

### Two Scoops of Django 3.x: Best Practices for the Django Web Framework, by [Daniel Feldroy](https://twitter.com/pydanny/) and [Audrey Feldroy](https://twitter.com/audreyr)

*Two Scoops of Django* is not a good resource to read immediately after *Python Crash Course*. It is, however, a really good book to be aware of as you gain more experience with Django. TSD is aimed at people who have built a number of Django projects, and are looking to better understand how to manage all the working parts of a significant webapp project built in Django. The recommendations in this book come from years of experiencing building and maintaining many Django-based sites of various sizes, and years of training professional Django developers.

You can see a full table of contents and order an electronic version of the book [here](https://www.feldroy.com/collections/everything/products/two-scoops-of-django-3-x). A print version of the book should be available soon.

![](../../images/recommended_reading/tsd_cover.jpg)

[top](#top)

### The Linux Command Line (2nd Edition), by [William Shotts](https://twitter.com/William_Shotts/)

Most Django projects are deployed to Linux-based servers, and if you're going to continue working with Django it will certainly help to be familiar with the Linux command line. Even if you deploy to a platform like Heroku that tries to automate most of the deployment work for you, you'll still need to use the command line at times to do things like creating a superuser on your live site, or run migrations. Even if you use Heroku's admin panel for some of these tasks, it's inevitable that at some point you'll need to use a command line for troubleshooting, or to run specific commands that don't have a browser-based GUI. *The Linux Command Line* is a great resource, and you can either read it straight through or skim it and focus on the sections that seem most relevant to your work.

If you buy the book [direct from No Starch Press](https://nostarch.com/tlcl2) you get a free ebook with the printed copy. You can also buy it from [Barnes and Noble](https://www.barnesandnoble.com/w/the-linux-command-line-2nd-edition-william-shotts/1132292602/) or [Amazon](https://www.amazon.com/Linux-Command-Line-2nd-Introduction-dp-1593279523/dp/1593279523/). You can see more information about using Linux at the author's site, [linuxcommand.org](http://linuxcommand.org/tlcl.php), where you can also download a free PDF version of the book.

![](../../images/recommended_reading/lcl_cover.jpg)

[top](#top)

### How Linux Works (2nd Edition), by Brian Ward

There's some overlap between this and *The Linux Command Line*, but if you enjoy learning about Linux this is another great book to read straight through, or skim and focus on the parts most relevant to your work. *How Linux Works* has been a mainstay in the Linux world for many years, and if you're continuing in web development it's well worth your time.

If you buy the book [direct from No Starch Press](https://nostarch.com/howlinuxworks2) you get a free ebook with the printed copy. You can also buy it from [Barnes and Noble](https://www.barnesandnoble.com/w/how-linux-works-2nd-edition-brian-ward/1126896249/) or [Amazon](https://www.amazon.com/How-Linux-Works-2nd-Superuser/dp/1593275676/).

![](../../images/recommended_reading/hlw_cover.jpg)

[top](#top)

### Practical SQL, by [Anthony DeBarros](https://twitter.com/anthonydb)

Django's Object Relational Mapper, or ORM as it's commonly referred to, is a tool that allows you to query for data from a database by writing pure Python. Django converts this to Structured Query Language, or SQL as it's commonly called. The ORM is an amazing tool that's made working with databases much easier over the years. But the farther you go with Django, the more an understanding of SQL will help you. It will help you write more efficient queries, even if you only never actually write raw SQL yourself. *Practial SQL* uses Postgres to teach you SQL, and Postgres is one of the most common databases that Django developers use.

If you buy the book [direct from No Starch Press](https://nostarch.com/practicalSQL) you get a free ebook with the printed copy. You can also buy it from [Barnes and Noble](https://www.barnesandnoble.com/w/practical-sql-anthony-debarros/1126049058/) or [Amazon](https://www.amazon.com/Practical-SQL-Beginners-Guide-Storytelling/dp/1593278276/). The code, data, and other online resources are available at [the author's GitHub page](https://github.com/anthonydb/practical-sql).

![](../../images/recommended_reading/psql_cover.jpg)

[top](#top)

---

## Online Resources

### Official Django Documentation

Django's official documentation is some of the clearest technical documentation you'll find for an open source project. It's well-organized and has clear and accurate writing throughout. Here's a brief list of sections to start looking at:

- The Django home page is at [djangoproject.com](https://www.djangoproject.com). Here's you'll find some highlights of the framework, and a bunch of information for Django developers of all levels.
- The [download](https://www.djangoproject.com/download/) page tells you how to install the latest official version. But it also lets you download development versions of upcoming releases, so you can see whether your code will continue to work on upcoming versions. You can also see a chart of how long each version will receive updates.
- The main page for the technical documentation is at [docs.djangoproject.com](https://docs.djangoproject.com/en/3.0/). Here you'll find installation instructions, a lengthy tutorial, places to get help, a guide to the overall documentation, and numerous ways to start exploring different areas of the documentation.
- There's a [community](https://www.djangoproject.com/community/) page that links to an active forum, a couple mailing lists, an IRC channel, and more.
- The Django code is in a [GitHub repository](https://github.com/django/django). Django is a large project so it will probably take you a while to start understanding how the codebase works, but it's a great example of a well-architected larger project.
- There's an [issue tracker](https://code.djangoproject.com) where people can report and work on bugs and other issues with the framework itself.
- The [about](https://www.djangoproject.com/foundation/) page covers the Django Software Foundation, and how you can get involved in supporting development and maintenance of Django.

If you're going to continue working with Django, you'll almost certainly be spending time reading through the official documentation. If you haven't done so already, take a quick look now so it's familiar when you need it.

### Learn Django

*Learn Django* is Will Vincent's site, which has a variety of Django resources including the books described above. Will recently reorganized his online resources at [learndjango.com](https://learndjango.com). The site highlights his books, but there's also a collection of excellent [tutorials](https://learndjango.com/tutorials/) about a variety of specific Django topics.

### Simple is Better Than Complex

[Vitor Freitas](https://twitter.com/vitorfs) started a [blog](https://simpleisbetterthancomplex.com) a while back about Python and Django, and I've found his articles and tutorials quite helpful as I've worked on numerous projects. It's worth checking out, and if you see one of his tutorials in your search results, it's probably a good resource to use.

### r/django

The [r/django](https://www.reddit.com/r/django/) subreddit has over 70k members, so it's a fairly active community. If you have questions as you work through your own projects, this is a pretty reasonable place to ask for help.

[top](#top)

---

## Podcasts

[top](#top)

---

## Talks

[top](#top)

---

## Libraries and Packages

[top](#top)

---