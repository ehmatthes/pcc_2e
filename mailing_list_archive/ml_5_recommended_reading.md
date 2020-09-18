---
layout: default
title: Recommended Reading, Django 3.1, and more (9/3/20)
parent: Mailing List
nav_order: 960
---

## 9/3/20
{: .no_toc }

---

# Recommended Reading, Django 3.1, and more
{: .no_toc }

Like many people, my working life has been diminished by all that's going on right now. But over the summer I was able to create a few new resources you might be interested in. I've written up a set of recommendations for what to read after finishing Python Crash Course, and I've written a few Python-focused articles that might be helpful as well.

My email was not forwarding correctly for a while, so if you replied directly to one of these emails I may not have gotten back to you. I apologize for that, and the issue has been resolved. If you have any questions related to the materials I'm sharing, please feel free to reach out.

* 
{:toc}

## Recommended Reading

One of the questions I've been asked most often over the years is, "I just finished reading Python Crash Course. Do you have any suggestions for what I should read next?"

There's a lot that goes into answering that question, so I added a section called [Recommended Reading](https://ehmatthes.github.io/pcc_2e/recommended_reading/recommended_reading/). Resources include books, websites, podcasts, talks, and newsletters. The recommendations are organized into four sections:
- First Steps
- General Python Resources
- Data Science Resources
- Django Resources


## Django 3.1 is out

Django 3.1 was released on August 4, 2020. Here's an [overview of what's new](https://ehmatthes.github.io/pcc_2e/updates/django3_1/), with a brief discussion of how to think about upgrading Django projects. There's one minor update to the book, which only impacts the deployment section in Chapter 20.

## Review: Serious Python

I didn't read very many books during the years I was teaching full time and writing Python Crash Course. I've been trying to read more lately, and one of the first books I turned to was Serious Python. It was excellent, and here's a [full review](https://ehmatthes.com/blog/review_serious_python/).

## What's faster than strptime()?

The function strptime() takes in a string, and returns a datetime object. While working on a data analysis project, I noticed my project was spending over 2 seconds just running strptime() on each datapoint. At first I thought there was nothing I could do about this. Then I started considering other ways to convert strings to datetime objects, and found many ways that are faster.

This article focuses on strptime(), but also shows how to examine a piece of code that's becoming a bottleneck in performance as a project grows. You can run the code in the article and benchmark different approaches on your own system if you're interested. The article is [here](https://ehmatthes.com/blog/faster_than_strptime/).

## Cleaning up a messy, exploratory Python project

Over the last year, I've been contributing to a project that aims to assess the risk of landslides in southeast Alaska in real time. My focus has been analyzing data from a stream gauge to determine whether the behavior of a local river can be used to assess landslide risk effectively enough to contribute to a monitoring and warning system.

This was an exploratory project at first, because no one knew if stream gauge data was relevant to landslide monitoring. The project has proven worthwhile, so I had to clean up what had become a really messy but important project. [This article](https://ehmatthes.com/blog/messy_python_project/) shows how I used the lessons from Serious Python to guide my cleanup work, with a focus on performance. If you're interested you can download a copy of the project and run the original version on your system, and try each of the optimizations that are discussed.

## PCC cover issue

Some people have been reporting that the cover is falling off their copy of Python Crash Course. No Starch Press focuses on producing high-quality books, and they've used a special lay-flat binding for many years. This binding, when properly made, is not attached in the middle of the spine so that when you open the book and lay it flat the spine doesn't crack. In one or two printings the cover was not attached correctly on some books, and the cover pulls off the book completely. This issue should be resolved in more recent printings.

You can see what the binding is supposed to look like in a [blog post](https://nostarch.com/blog/lay-flat-bindings-what-and-how) from No Starch. If your copy is defective and the cover has come off, you can write to info@nostarch.com, and they will replace your copy at no cost. I'm sorry if you are dealing with this issue.

## In the Works

I'm working on a number of different resources, and I'll share them as they're each ready:
A section highlighting projects that readers have made, based on what they've learned from PCC
A section where readers share their stories about trying to find a programming-related job
A cheat sheet for using Git to manage your projects
Solutions for Chapters 12-14, and Chapters 18-20

## Feedback

If you have questions or comments about these new sections or anything related to Python Crash Course, feel free to reply to this email. You can also find me on Twitter [@ehmatthes](https://twitter.com/ehmatthes). Thanks!

Eric

---

[top](#top)