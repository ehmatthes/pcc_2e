---
layout: default
title: Third printing
parent: Updates
nav_order: 30
---

# Updates and Errata - Third printing

This page is broken into two parts, Updates and Errata. *Updates* address issues that affect whether your code will run or not. *Errata* refer to minor issues such as typos, and errors in grayed-out code that probably won't affect the code you're entering.

## Updates

All of the code in the third printing should work; if you find any code that doesn't run, please let me know. You can reach me through email at ehmatthes@gmail.com, or on Twitter at [@ehmatthes](https://twitter.com/ehmatthes).

---

## Errata

### Chapter 6

On page 100, the order of the output for *user.py* should match the order in which keys were inserted into the dictionary.

### Chapter 7

On page 125, `pop()` is referred to as a function. This function only acts on an object, so it is more properly called a method.

### Chapter 13

On page 262 in the code snippet that calculates the value for `number_rows`, `available_height_y` should be `available_space_y`. The listing on page 263 that uses this code is correct.

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
