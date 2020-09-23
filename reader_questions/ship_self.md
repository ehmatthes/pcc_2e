---
layout: default
title: Role of self and ai_game in code that creates the ship
parent: Reader Questions
nav_order: 10
---

# What is the role of self and ai_game in the code that creates the ship?
{: .no_toc }

## Overview

People have written a number of times to ask about the role of `self` and `ai_game` in the code that creates the ship. This isn't surprising, because there's a lot going on in just a couple lines of code. It also took me a while to come up with this approach when revising the game for the second edition of the book.

In the first edition of the book, the entire game was function-based. That was a simpler approach initially, but it got pretty confusing towards the end of the project because the function definitions and function calls had lots of parameters. In the second edition, the entire game is class based. It's a little more confusing at first, but this approach pays off quickly as there are very few parameters to pass around. So let's look at what's happening when we first create a Ship object.

## The role of self in AlienInvasion

I'm looking at the version of Alien Invasion that's covered  on pages 232-236; you can find that code [here](https://github.com/ehmatthes/pcc_2e/tree/master/chapter_12/adding_ship_image). 

Let's look at the part of `AlienInvasion` where we make a ship:

```python
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
```

The last line shown here is the line that creates the ship object. Let's consider the meaning of `self` in the line

```
        self.ship = Ship(self)
```

The variable `self` almost always refers to an instance of the current class. What's the current class? This line appears in the `AlienInvasion` class, so the `self` here refers to an instance of `AlienInvasion`. This is the same object that we create at the end of the file:

```python
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
```

The variable `ai` in this block of code and the variable `self` in `AlienInvasion` both refer to the same thing.

To really see this, we can insert a `print()` call in the `__init__()` method right after we make the ship:

```python
    def __init__(self):
        ...
        self.ship = Ship(self)
        print(f"\nself in AlienInvasion: {self}")
```

Now when we run the game, here's what we see in the terminal:

```
pygame 2.0.0.dev8 (SDL 2.0.12, python 3.8.2)
Hello from the pygame community. https://www.pygame.org/contribute.html

self in AlienInvasion: <__main__.AlienInvasion object at 0x10ca35670>
```

The first two lines are generated every time we run the game. But the last line shows us exactly what `self` refers to at this point in the program: an `AlienInvasion` object associated with the file named `__main__`.

## The role of self and ai_game in Ship

Now let's look at the relevant code in `Ship`:

```python
class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        ...
```

We don't really need to look at much code here, because the question people usually ask is, What do `self` and `ai_game` refer to in the definition of `__init__()`?

As mentioned earlier, the variable `self` refers to an object of the current class. So `self` here should refer to a `Ship` object. Let's throw in a couple `print()` calls and see if this is true:

```python
    def __init__(self, ai_game):
        print(f"\nself in Ship: {self}")
        print(f"ai_game in Ship: {ai_game}")
        """Initialize the ship and set its starting position."""
        ...
```

Here's the output when we run *alien_invasion.py* now:

```
pygame 2.0.0.dev8 (SDL 2.0.12, python 3.8.2)
Hello from the pygame community. https://www.pygame.org/contribute.html

self in Ship: <ship.Ship object at 0x1108134c0>
ai_game in Ship: <__main__.AlienInvasion object at 0x10feb6670>

self in AlienInvasion: <__main__.AlienInvasion object at 0x10feb6670>
```

We can see that the `self` in Ship refers to a `Ship` object, in the file named `ship`. The `ai_game` in Ship refers to an `AlienInvasion` object, associated with the file named `__main__`. We can even see from the other `print()` call we made earlier that these two `AlienInvasion` objects are the same, since they're at the same point in memory: `0x10feb6670`.

## Conclusion and takeaways

It's quite reasonable to be confused by all of this.

First of all, the variable `self` refers to different things in different files. This confusion comes up in just about every object-oriented programming language. In JavaScript this variable is usually referred to as `this`, and there are as many questions online about JavaScript's `this` as there are about Python's `self`.

Also, when we create a ship object we're only passing one argument: `self.ship = Ship(self)`. But this is being passed to a method that has two parameters: `def __init__(self, ai_game)`. It's structured this way because every method in a class is automatically passed a reference to the current object. You could call it anything you want, but the convention in Python is to call the first parameter in any method definition `self`. So Ship's `__init__()` method receives two arguments: the reference to the current ship object that's passed automatically by Python, and the reference to the `AlienInvasion` object that we're passing from `AlienInvasion`.

I hope you've enjoyed this discussion, but please don't feel like you need to understand this fully to move forward in the project. This is a little complexity in the initial setup of the project, that makes the rest of the project much simpler and easier to reason about. When you start a new game, you should feel free to copy this initial structure without memorizing it, or even fully understanding it. It will only really make sense fully when you've worked with classes and objects in enough variety of contexts to start recognizing the general patterns.

*Note: At some point you'll come across static methods. These are methods that don't need a reference to the current object, so they don't need a `self` parameter in their function definitions. Static methods are marked with `@staticmethod` on the line immediately preceding the method's definition.*