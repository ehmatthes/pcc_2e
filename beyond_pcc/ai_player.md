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

Start by making a new file called *ai_player.py*, in the same directory as *alien_invasion.py*. We'll do everything from here on out in *ai_player.py*; the point of this is to automate the game play without touching any of the original game code.

To automate the game play, we need to make an instance of AlienInvasion. We would normally call `run_game()` to start a game, but that would start the main game loop and we'd never be able to take control except by using the keyboard. Instead, we'll write our own class called `AIPlayer`, and we'll give this class the game object. Then we'll write a new `run_game()` method, where we can interject code that controls the elements of the game.

Here's the core structure of the `AIPlayer` class:

```python
from alien_invasion import AlienInvasion

class AIPlayer:

    def __init__(self, ai_game):
        """Automatic player for Alien Invasion."""

        # Need a reference to the game object.
        self.ai_game = ai_game

    def run_game(self):
        """Replaces the original run_game(), so we can interject our own
        controls.
        """

        # Start out in an active state.
        self.ai_game.stats.game_active = True

        # Start the main loop for the game.
        while True:
            # Still call ai_game._check_events(), so we can use keyboard to
            #   quit.
            self.ai_game._check_events()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()

            self.ai_game._update_screen()

if __name__ == '__main__':
    ai_game = AlienInvasion()

    ai_player = AIPlayer(ai_game)
    ai_player.run_game()
```

We blah

When you run this file, the game will start automatically. You could play the game with the keyboard, because we're calling the original `_check_events()`. Instead, let's write one line of code that fires bullets whenever possible:

```python
class AIPlayer:

    def __init__(self, ai_game):
        """Automatic player for Alien Invasion."""

        # Need a reference to the game object.
        self.ai_game = ai_game

    def run_game(self):
        """Replaces the original run_game(), so we can interject our own
        controls.
        """

        # Start out in an active state.
        self.ai_game.stats.game_active = True

        # Start the main loop for the game.
        while True:
            # Still call ai_game._check_events(), so we can use keyboard to
            #   quit.
            self.ai_game._check_events()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()
                self.ai_game._fire_bullet()

            self.ai_game._update_screen()
```

This one line of code is a call to `ai_game.fire_bullet()`, which runs on every pass through the main loop as long as the game as active.

Now when you run the game, the ship will always fire a bullet whenever there are fewer than 3 bullets on the screen. It may look like one bullet at first, because the first three bullets are fired on the first three game cycles.

This is really satisfying, because we can sit back and watch the ship fire bullets all by itself. But it's not a very good game strategy. If we let this play until the game ends, the ship will only ever destroy the aliens in the middle columns, and then rest of the aliens will creep down and hit the ground. To make things more interesting, we need to make the ship move.

Now that you've seen how to take control of the game, feel free to try automating the ship's movement on your own. See [Challenge blah]() if you're interested in trying this on your own before moving on.

sweep

speed up for development work

targeting a specific alien




Try It Yourself: Add sounds that play when the game starts, when the ship is hit, and when the game is over. You might also want to add sounds for other events like passing certain scoring milestones.