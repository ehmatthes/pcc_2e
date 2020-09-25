---
layout: default
title: Fourth printing
parent: Updates
nav_order: 40
---

# Updates and Errata - Fourth printing
{: .no_toc }

This page is broken into two parts, Updates and Errata. *Updates* address issues that affect whether your code will run or not. *Errata* refer to minor issues such as typos, and errors in grayed-out code that probably won't affect the code you're entering.

If you find an error in the book or can't get something to work, please let me know. You can reach me through email at ehmatthes@gmail.com, or on Twitter at [@ehmatthes](https://twitter.com/ehmatthes).

* 
{:toc}

---

## Updates

### Chapter 17

##### Running *hn_submissions.py* sometimes results in a KeyError (page 373)

The program *hn_submissions.py* makes a series of API calls to get information about each of the articles on the front page of [Hacker News](https://news.ycombinator.com). When processing the data associated with each article, the code looks for the `'descendants'` key, which tells us how many comments the article has associated with it. Hacker News is maintained partially as a promotional tool for the startup accelerator [YCombinator](https://www.ycombinator.com), and YC companies can make special posts on Hacker News that are exempt from comments. For example, YC companies can make hiring posts that sit on the front page of HN for a while, with comments disabled.

If you run *hn_submissions.py* when one of these posts is on the front page, you'll get a `KeyError` because there is no `'descendants'` key for these posts. This doesn't happen all that often, but if you run into this issue you can catch the `KeyError` and continue the loop when one of these posts is present:

```python
-- snip --
for submission_id in submission_ids[:30]:
    -- snip --
    # Build a dictionary for each article.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        # This is a special YC post with comments disabled.
        continue
    else:
        submission_dicts.append(submission_dict)
-- snip --
```

### Chapter 20

##### The `psycopg2` package (page 448)

There's one minor change you'll need to make in order to deploy your Learning Log project to Heroku. On page 448 in the section *Installing Required Packages*, it says to install the package `psycopg2==2.7.*`. This should be changed to `psycopg2-binary`.

##### Heroku settings (page 456)

If you're using [Django 3.1](../django3_1), which was released on August 4, 2020, you'll need to add one line to the code on page 456. The *settings.py* file no longer imports the `os` module by default, so we need to import it when we create the Heroku-specific settings for deployment.

On page 456, add `import os` right before the line that imports `django_heroku`:

```python
# Heroku settings.
import os
import django_heroku
django_heroku.settings(locals())
--snip--
```

##### The Python Runtime (page 449)

The latest Python runtimes available on Heroku are listed [here](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version). The ones you're probably interested in are `python-3.8.5` and `python-3.7.8`. You can use either of these in the *runtime.txt* file described on page 449.

This is not a critical update; if you specify a runtime that's slightly out of date, Heroku will use the closest match it finds in its available runtimes.

## Errata

No errata have been reported for the fourth printing at this time.