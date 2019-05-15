---
layout: default
title: First printing
parent: Updates
nav_order: 10
---

# Updates - First printing

## Chapter 9

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