---
layout: default
title: Chapter 13
parent: Solutions
nav_order: 104
---

# Solutions - Chapter 13
{: .no_toc }

The solutions for Chapters 12-14 are kept in a [separate repository](https://github.com/ehmatthes/pcc_2e_ai_solutions), because every exercise is a mini project. This page contains links to individual solutions in the repository.

If you haven't already seen the [cheat sheets](../../cheat_sheets/cheat_sheets/), there's a sheet that focuses on Pygame which you might find helpful when working on these exercises.

Also, it's helpful to have a look through some of the [Pygame documentation](https://www.pygame.org/docs/) as you work on these exercises. There are also direct links to specific pages in the documentation that are helpful for certain exercises.

---

* 
{:toc}

Back to [solutions](../solutions).

---

## 13-1: Stars

Find an image of a star . Make a grid of stars appear on the screen.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_13/solution_13_1)

## 13-2: Better Stars

You can make a more realistic star pattern by introducing randomness when you place each star. Recall thatyou can get a random number like this:

```python
from random import randint
random_number = randint(-10, 10)
```

This code returns a random integer between -10 and 10. Using your code in Exercise 13-1, adjust each star's position by a random amount.

Note: *This is a basic solution that shows working code to solve this exercise. If you want, you can experiment with different size stars, different spacing values, and different values for the amount of randomness in each star's position. From my experimentation this effect seems to work better with a relatively dense field of smaller stars.*

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_13/solution_13_2)

## 13-3: Raindrops

Find an image of a raindrop and create a grid of raindrops. Make the raindrops fall toward the bottom of the screen until they disappear.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_13/solution_13_3)

## 13-4: Steady Rain

Modify your code in Exercise 13-3 so when a row of raindrops disappears off the bottom of the screen, a new row appears at the top of the screen and begins to fall.

Note: *This is a simple working solution as well, and has not been optimized. If you like this exercise I encourage you to experiment with different size drops, different approaches to defining the starting position for each drop, and different approaches to creating new rows of raindrops.*

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_13/solution_13_4)

## 13-5: Sideways Shooter Part 2

We've come a long way since Exercise 12-6, Sideways Shooter. For this exercise, try to develop Sideways Shooter to the same point we've brought *Alien Invasion* to. Add a fleet of aliens, and make them move sideways toward the ship. Or, write code that places aliens at random positions along the right side of the screen and then sends them toward the ship. Also, write code that makes the aliens disappear when they're hit.

Note: *This is a solution to the version that sends individual aliens across the screen at random intervals.*

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_13/solution_13_5)

## 13-6: Game Over

In Sideways Shooter, keep track of the number of times the ship is hit and the number of times an alien gets past the ship. Decide on an appropriate condition for ending the game, and stop the game when this situation occurs.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_13/solution_13_6)