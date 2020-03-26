---
layout: default
title: Pygame - Adding Sound and Automating Game Play
parent: Beyond PCC
nav_order: 25
---

# Pygame - Adding Sound and Automating Game Play
{: .no_toc }

This section is broken into two parts. The first part focuses on adding sound to your Alien Invasion project, and the second focuses on writing a separate program that plays the game automatically. Adding sound doesn't take much code, but it makes the game much more interesting. Automating game play is more complicated, but it can also be a really interesting and satisfying exercise.

* 
{:toc}

---

## Adding Sound

If you want to take this as a challenge before reading this guide, feel free to look at the Pygame documentation, and see if you can add sounds on your own. In this guide, we're going to play a firing sound each time the ship fires a bullet, and an explosion sound each time an alien is shot down.

### The Pygame Mixer module

The Pygame Mixer Module manages music and sound effects. You can take a look at the [documentation](https://www.pygame.org/docs/ref/mixer.html); I also found this [Nerd Paradise post](https://nerdparadise.com/programming/pygame/part3) helpful.

There are lots of resources for finding sound effects. I found some useful ones at [blah](). I chose [this sound]() for firing bullets, and [this sound]() for an alien being hit. Make a new folder in your *alien_invasion* folder called *sounds*. This folder should be at the same directory level as your *images* folder.

### The *sound_effects.py* file

We'll start by making a new file called *sound_effects.py*, where we can store all of the sound effects we'll use in the game. This file is pretty short:

```python
import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('sounds/laser1.wav')
alien_sound = pygame.mixer.Sound('sounds/Explosion_02.wav')
```

We import `pygame`, and then initialize the `mixer` module. Then we define two sounds, `bullet_sound` and `alien_sound`. To make a sound in Pygame, you make an instance of the [Sound](https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound) class, with a path to the sound file as the only argument.

### Modifying *alien_invasion.py*

Now we need to modify *alien_invasion.py* so the sounds play at the right times. At the top of the file, import the sound effects module we just created:

```python
import sys
from time import sleep

import pygame

from settings import Settings
--snip--
from alien import Alien
import sound_effects as se


class AlienInvasion:
    --snip--
```

You can add this import statement after all of the existing import statements.

To make a firing sound, we call the `play()` method on the `Sound` object each time a bullet is fired. We make this call from `_fire_bullet()`:

```python
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            se.bullet_sound.play()
```

When you play the game now, you should hear a sound every time you fire a bullet.

To make a sound when an alien is hit, we modify the `_check_bullet_alien_collisions()` method:

```python
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            se.alien_sound.play()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            --snip--
```

We play the alien sound whenever there's a `collisions` dictionary, indicating that at least one alien has just been destroyed.

Now your game should sound much more interesting! You should hear a steady stream of sounds as you fire bullets and destroy aliens. You might also want to add sounds for destroying all aliens in the fleet, and when an alien hits the ship.

## Automating Game Play

This is the really interesting part. If you want to try this on your own before reading ahead, you can see the [challenges here](). If you're new to programming, though, getting this set up can be pretty challenging. It's perfectly reasonable to read through this guide to get started, and then explore further automation algorithms on your own.

### Firing automatically

Let's start out by writing a program that takes control of the ship, and fires as often as possible.

fire

sweep

speed up for development work

targeting a specific alien




Try It Yourself: Add sounds that play when the game starts, when the ship is hit, and when the game is over. You might also want to add sounds for other events like passing certain scoring milestones.