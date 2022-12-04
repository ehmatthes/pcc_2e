---
layout: default
title: First printing
parent: Updates
nav_order: 10
---

# Updates and Errata - First printing
{: .no_toc }

This page is broken into two parts, Updates and Errata. *Updates* address issues that affect whether your code will run or not. *Errata* refer to minor issues such as typos, and errors in grayed-out code that probably won't affect the code you're entering.

If you find an error in the book or can't get something to work, please let me know. You can reach me through email at ehmatthes@gmail.com, or on Twitter at [@ehmatthes](https://twitter.com/ehmatthes).

* 
{:toc}

---

## Updates

### Chapter 9

In the section *Working with Classes and Instances*, we build a class that represents a car. One method in the class provides a descriptive name of the car:

```python
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
```

The attribute `self.manufacturer` should be `self.make`. This was incorrect in the new code at the top of page 163, and in the grayed-out code on pages 168 and 174.

The correct code should be:

```python
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
```

[top](#top)

### Chapter 12

*This only applies if you're using Python 3.8.*

The stable version of Pygame has not been updated to work with Python 3.8 yet. However, there is a recent development version that works with Python 3.8. To install it, run the following command:

    $ python -m pip install pygame==2.0.0.dev6

You should use the same command you use to run a Python terminal session on your system, which might be `python`, `python3`, `py`, `python3.8`, or something else.

If you've had any issues running Pygame on macOS, this version of Pygame should address those issues as well.

[top](#top)

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

[top](#top)

### Chapter 20

See [Deploying Django Projects](../../deploying_django).

[top](#top)

---

## Errata

### Chapter 6

On page 100, the order of the output for *user.py* should match the order in which keys were inserted into the dictionary.

On page 102, in *Looping Through All the Keys in a Dictionary*, the first print call should start with "Hi ":

```python
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
```

On page 109, the code that prints each topping should use f-strings:

```python
for topping in pizza['toppings']:
    print(f"\t{topping}")
```

### Chapter 7

On page 125, `pop()` is referred to as a function. This function only acts on an object, so it is more properly called a method.

### Chapter 9

On page 176, in the grayed-out code for the `__init__()` method of the `Battery` class, the value of `battery_size` should be 75.

### Chapter 10

On page 185, the line `print(contents.rstrip())` should be indented at the left margin.

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

