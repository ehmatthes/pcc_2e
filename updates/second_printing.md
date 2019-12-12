---
layout: default
title: Second printing
parent: Updates
nav_order: 20
---

# Updates and Errata - Second printing
{: .no_toc }

This page is broken into two parts, Updates and Errata. *Updates* address issues that affect whether your code will run or not. *Errata* refer to minor issues such as typos, and errors in grayed-out code that probably won't affect the code you're entering.

* 
{:toc}

---

## Updates

### Chapter 12

*This only applies if you're using Python 3.8.*

The stable version of Pygame has not been updated to work with Python 3.8 yet. However, there is a recent development version that works with Python 3.8. To install it, run the following command:

    $ python -m pip install pygame==2.0.0.dev6

You should use the same command you use to run a Python terminal session on your system, which might be `python`, `python3`, `py`, `python3.8`, or something else.

If you've had any issues running Pygame on macOS, this version of Pygame should address those issues as well.

[top](#top)

### Chapter 20

##### The `psycopg2` package (page 448)

There's only one minor change you'll need to make in order to deploy your Learning Log project to Heroku. On page 448 in the section *Installing Required Packages*, it says to install the package `psycopg2==2.7.*`. This should be changed to `psycopg2-binary`.

##### The Python Runtime (page 449)

The latest Python runtimes available on Heroku are listed [here](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version). The ones you're probably interested in are `python-3.8.0` and `python-3.7.5`. You can use either of these in the *runtime.txt* file described on page 449.

This is not a critical update; if you specify a runtime that's slightly out of date, Heroku will use the closest match it finds in its available runtimes.

[top](#top)

---

## Errata

### Chapter 6

On page 100, the order of the output for *user.py* should match the order in which keys were inserted into the dictionary.

### Chapter 7

On page 125, `pop()` is referred to as a function. This function can only be called through an object, so it is more properly called a method.

### Chapter 13

On page 262 in the code snippet that calculates the value for `number_rows`, `available_height_y` should be `available_space_y`. The listing on page 263 that uses this code is correct.

### Chapter 15

On page 323, in exercise 15-3, `plt.scatter()` should be `ax.scatter()` and `plt.plot()` should be `ax.plot()`.

### Chapter 19

On page 414, the line that sets the value for `labels` should have empty quotes:

```python
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
```

The code works fine as it's written, but the new entry page will differ slightly from the screenshot shown on page 417.

### Index

On page 497, the entry for *Discord* should point to page 484, not page 48.

[top](#top)

