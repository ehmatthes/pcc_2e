---
layout: default
title: Random Functions
parent: Beyond PCC
nav_order: 10
---

# Random Funtions
{: .no_toc }

Randomness is a really important and useful topic in programming. It can be used to do simple things like choose which player goes first in a game, or draw a random card from a deck. It can also be used for critically important processes like allowing a user to reset a forgotten password.

All of this code uses functions from the `random` module, which is included in the Python Standard Library. You might be curious to look at the [documenation for the `random` module](https://docs.python.org/3/library/random.html).

* 
{:toc}

---

## Generating a random number between 0 and 1

The following code generates a random number between 0 and 1. The number may be 0, but it will always be less than 1:

```python
from random import random

random_num = random()
print(random_num)
```

```
0.32763594489253733
```

## Generating a random integer

If you want a single random number from a certain range, use the `randint()` function. The function will return a random number in the given range, including the upper and lower bound you specify.

```python
from random import randint

random_int = randint(1, 6)
print(rand_int)
```

```
3
```

## Choosing a random element from a list

If you want to choose a single random element from a list, use the `choice()` function. The selected element is not removed from the list.

```python
from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
random_player = choice(players)
print(random_player)
```

```
charles
```

## Putting a list in random order

To put a list into random order, use the `shuffle()` function.

```python
from random import shuffle

players = ['charles', 'martina', 'michael', 'florence', 'eli']
shuffle(players)

print(players)
```

```
['florence', 'eli', 'charles', 'martina', 'michael']
```

This function changes the order of the list, and you can't get the original order back. If you want to keep the original order, pass a copy of the list to the `shuffle()` function:

```python
from random import shuffle

players = ['charles', 'martina', 'michael', 'florence', 'eli']

shuffled_players = players[:]
shuffle(shuffled_players)

print(players)
print(shuffled_players)
```

```
['charles', 'martina', 'michael', 'florence', 'eli']
['martina', 'eli', 'charles', 'michael', 'florence']
```

