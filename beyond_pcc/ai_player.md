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

**Try It Yourself:** Add sounds that play when the game starts, when the ship is hit, and when the game is over. You might also want to add sounds for other events like passing certain scoring milestones.

[top](#top)

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

We define a class called `AIPlayer`. This is a simple class; it does not inherit from `AlienInvasion`, although it's perfectly reasonable to try that approach. The code you end up with using inheritance is a little less verbose, but it's also a little harder to reason about. If you're curious, feel free to try building an `AIPlayer` class that does inherit from `AlienInvasion`. One advantage is that you'll have more direct access to elements of the game, but there will also be a less clear distinction between what's part of the original game, and what's part of the automated player.

In the approach shown here, the `AIPlayer` class needs an instance of the `AlienInvasion` class. The game object needs to be passed as an argument to `__init__()`, and we call this attribute `ai_game`. We attach it to `self`, to make sure the game object is available throughout the `AIPlayer` class.

If we call the original `run_game()` method from `AlienInvasion`, we'll start a while loop that won't let us control any of the game elements. So instead we write a new `run_game()` method that we can call in place of the original `run_game()` method. This method needs to do anything that the original `run_game()` method did, but we'll be able to add code to this method when we want to take control of some of the game elements.

In `run_game()`, we need the game to start out in an active state because we want it to start playing immediately. So we set `game_active` to `True`. We access game elements through the game object, so this line is written:

```python
self.ai_game.stats.game_active = True
```

It's worth looking closely at this line, because this is how we'll approach many aspects of automating the game play. The `self` here refers to an instance of `AIPlayer`, not `AlienInvasion`. The `ai_game` attribute refers to an instance of the `AlienInvasion` class, which represents the game as a whole. We then access the `stats` attribute in `AlienInvasion`, which refers to an instance of the `GameStats` class. Finally, we access the `game_active` attribute of `GameStats`, and set it to `True`.

Next we need a while loop, so the automated game will do all of the updating that was being done in the original `run_game()` method. We still want to call the original `_check_events()`, because we'll want to be able to quit the game at some point. If the game is active, we still need to update the ship, update the bullets, and update the aliens. Finally, we need to update the screen on every pass through the loop. Since we need to do this when the game is active or inactive, the call to `_update_screen()` occurs outside of the if block.

When we run this file, we need to make an instance of `AlienInvasion`, which we assign to `ai_game`. Then we need to make an instance of `AIPlayer`, which requires the `ai_game` object as an argument. Finally, we call the `run_game()` method associated with the `ai_player` object, not the one associated with `ai_game`.

When you run this file, the game will start automatically. You could play the game with the keyboard, because we're calling the original `_check_events()`. Instead, let's write one line of code that fires bullets whenever possible:

```python
class AIPlayer:

    def __init__(self, ai_game):
        --snip--

    def run_game(self):
        --snip--

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

You might also notice that the mouse is visible when the game is playing. That's because the code that hides the mouse is in the `_check_play_button()` method, which we never call. We can add that line to `run_game()`:

```python
    def run_game(self):
        """Replaces the original run_game(), so we can interject our own
        controls.
        """

        # Start out in an active state, and hide the mouse.
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)

        # Start the main loop for the game.
        while True:
            --snip--
```

Make sure you also add an `import pygame` statement at the top of the file.

Now that you've seen how to take control of the game, feel free to try automating the ship's movement on your own. See [Challenge blah]() if you're interested in trying this on your own before moving on.

[top](#top)

### Moving the ship

We'll implement a really simple strategy now. We'll move the ship all the way to the right, firing whenever possible. Then we'll move the ship all the way to the left, again firing whenever possible. We'll do this over and over, until the game ends.

All of this can be coded right in the while loop of the `run_game()` method:

```python
        # Start the main loop for the game.
        while True:
            # Still call ai_game._check_events(), so we can use keyboard to
            #   quit.
            self.ai_game._check_events()

            # Sweep the ship right and left for the entire game.
            ship = self.ai_game.ship
            screen_rect = self.ai_game.screen.get_rect()

            if not ship.moving_right and not ship.moving_left:
                # Ship hasn't started moving yet; move to the right.
                ship.moving_right = True
            elif (ship.moving_right
                        and ship.rect.right > screen_rect.right - 10):
                # Ship about to hit right edge; move left.
                ship.moving_right = False
                ship.moving_left = True
            elif ship.moving_left and ship.rect.left < 10:
                ship.moving_left = False
                ship.moving_right = True

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()
                self.ai_game._fire_bullet()

            self.ai_game._update_screen()
```

We first make assign the `self.ai_game.ship` object to a variable called `ship`, so we don't have to type out the longer reference repeatedly. We do the same for `screen_rect`.

Then we run through three cases:

- If the ship is not moving at all, the game must have just started. In this case, we set `moving_right` to `True`.
- If the ship is moving right, and the right side of the ship is within 10 pixels of the right side of the screen, we change directions. We set `moving_right` to `False`, and set `moving_left` to `True`. (Remember if both of these are `True`, the ship will move both directions at once and remain in the same position.)
- If the ship is moving left and it gets within 10 pixels of the left edge of the screen, we change directions.

That's it! Now when you run the game the ship will sweep right and left, firing constantly. It will clear the first screen, and probably many more screens if you let it.

[video?]

[top](#top)

### Refactoring

The main while loop in `run_game()` is getting pretty long, so we should pull out the automation logic into a separate method. I made a new method called `_implement_strategy()`, and moved the code for moving the ship and firing bullets into this method:

```python
class AIPlayer:

    def __init__(self, ai_game):
        --init--

    def run_game(self):
        """Replaces the original run_game(), so we can interject our own
        controls.
        """

        # Start out in an active state, and hide the mouse.
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)

        # Start the main loop for the game.
        while True:
            # Still call ai_game._check_events(), so we can use keyboard to
            #   quit. Also call our own method to initiate events.
            self.ai_game._check_events()
            self._implement_strategy()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()

            self.ai_game._update_screen()

    def _implement_strategy(self):
        """Implement an automated strategy for playing the game."""

        # Sweep the ship right and left for the entire game.
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()

        if not ship.moving_right and not ship.moving_left:
            # Ship hasn't started moving yet; move to the right.
            ship.moving_right = True
        elif (ship.moving_right
                    and ship.rect.right > screen_rect.right - 10):
            # Ship about to hit right edge; move left.
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            ship.moving_left = False
            ship.moving_right = True

        # Fire a bullet whenever possible.
        self.ai_game._fire_bullet()
```

This is nice, because all of the code that handles the automation is in its own section of the file. Most of `_implement_strategy()` is currently focused on moving the ship. This method is going to get really long as soon as we start to do any other work, so let's move most of this code to a new method called `_control_ship()`:

```python
    def _implement_strategy(self):
        """Implement an automated strategy for playing the game."""
        self._control_ship()        

        # Fire a bullet whenever possible.
        self.ai_game._fire_bullet()

    def _control_ship(self):
        """Controls automated movement of the ship."""
        # Sweep the ship right and left for the entire game.
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()

        if not ship.moving_right and not ship.moving_left:
            # Ship hasn't started moving yet; move to the right.
            ship.moving_right = True
        elif (ship.moving_right
                    and ship.rect.right > screen_rect.right - 10):
            # Ship about to hit right edge; move left.
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            ship.moving_left = False
            ship.moving_right = True
```

This is nice and clear, and it should provide a consistent overall structure as we explore different strategies to optimize automated gameplay.

Watching the automated game play is fun and satisfying, but it can be a little slow to watch the automated game at regular speed. Next we'll add a little code that speeds up the game during our development work.

[top](#top)

### Speeding up the game for development work

When we want to see how effective a new automation strategy is, it would be nice to see the game play out more quickly than the standard speed that's good for human players. We can do this by modifying some of the games settings as a group.

To do this, we'll write a new method called `_modify_speed()`, which we can call from `run_game()`:

```python
class AIPlayer:

    def __init__(self, ai_game):
        --snip--

    def run_game(self):
        """Replaces the original run_game(), so we can interject our own
        controls.
        """

        # Start out in an active state, and hide the mouse.
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)

        # Speed up the game for development work.
        self._modify_speed(10)

        # Start the main loop for the game.
        while True:
            --snip--

    def _implement_strategy(self):
        --snip--

    def _control_ship(self):
        --snip--

    def _modify_speed(self, speed_factor):
        self.ai_game.settings.ship_speed *= speed_factor
        self.ai_game.settings.bullet_speed *= speed_factor
        self.ai_game.settings.alien_speed *= speed_factor
```

We want to be able to easily speed up the game when we're trying out new strategies, but also slow the game back down when we want to watch a game play out at the normal speed. We write `_modify_speed()` so it accepts an argument that controls how much to speed up the game. If you pass an argument of 1 the game will play at normal speed. Anything greater than 1 will speed up the game, and anything less than 1 will slow the game down.

In `_modify_speed()` we adjust the speed of the ship, the bullets, and the aliens.

Now when you play the game with a speed factor of something like 10, you'll see how effective the strategy is, and you'll see its weak points as well. For example I can see that the sweeping strategy is pretty effective at clearing out most of the fleet, but it's really inefficient when there's only one or two aliens left:

[video, commit 75c8b8]

You should be aware that speeding up the game affects the high score that your strategy will reach. You can see this by trying a couple very different speed factors. For example on my system a speedup scale of 10 with the current strategy ends with around 8,000,000 points at around level 18. With a speedup scale of 100, it only earns about 4,000 points, and it can't even clear the first screen. If you are comparing strategies, make sure you're using the same speed factor for each of your runs.

[top](#top)

### Randomized firing

One interesting idea is to give some slight randomness to the decision about whether to fire or not. Right now the ship is firing whenever it can. That means it immediately fires three bullets, and then fires every time a bullet hits an alien or disappears off the top of the screen. This means the bullets often end up in a tightly-packed group, especially when there's only one alien left and the ship is moving out of sync with the alien.

We can use the [random()](../../random_functions/) function to determine when to fire. The `random()` function returns a decimal between 0 and 1. So if we only fire when we get a random number less than 0.5, we'll fire a bullet on half of the game cycles where we can fire.

Here's what this looks like:

```python
import pygame

from random import random

from alien_invasion import AlienInvasion

class AIPlayer:
    --snip--

    def _implement_strategy(self):
        """Implement an automated strategy for playing the game."""
        self._control_ship()        

        # Fire a bullet whenever possible.
        firing_frequency = 0.5
        if random() < firing_frequency:
            self.ai_game._fire_bullet()
```

I don't think this approach helps the current strategy, but I have found it a useful approach in some situations. If you want, you can put this in a new method called `_fire_bullet()`, and give it a parameter for the firing frequency. Then you could use different firing frequencies in specific situations, such as when there are only a certain number of aliens left on the screen.

Next we'll look at targeting a specific alien.

[top](#top])

### Changing strategies mid-level

Clearly the sweeping approach works well to destroy most of the fleet. But it struggles when there's just one alien left, and most of the bullets just fly up through an empty screen. It seems a good idea to respond differently at the start of a level, than when there's only a partial fleet.

I don't want to give away all the best strategies, because it's a lot of fun to try different approaches. So I'll close out this guide by introducing two final ideas you can play with. The first is to use different strategies depending on the size of the remaining fleet. The second is to focus on a specific alien.

For a simple approach to implementing different strategies, let's stop moving when the fleet is cut in half. To help this we'll make a parameter that represents the size of a full fleet.

```python
class AIPlayer:

    def __init__(self, ai_game):
        --snip--

    def run_game(self):
        --snip--

        # Speed up the game for development work.
        self._modify_speed(10)

        # Get the full fleet size.
        self.fleet_size = len(self.ai_game.aliens)

        # Start the main loop for the game.
        while True:
            --snip--

    def _implement_strategy(self):
        """Implement an automated strategy for playing the game."""
        self._control_ship()        

        # Fire a bullet whenever possible.
        firing_frequency = 1.0
        if random() < firing_frequency:
            self.ai_game._fire_bullet()

    def _control_ship(self):
        """Controls automated movement of the ship."""

        # Sweep right and left until half the fleet is destroyed, then stop.
        if len(self.ai_game.aliens) >= 0.5 * self.fleet_size:
            self._sweep_left_right()
        else:
            self.ai_game.ship.moving_right = False
            self.ai_game.ship.moving_left = False

    def _sweep_left_right(self):
        """Sweep the ship right and left continuously."""
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()

        if not ship.moving_right and not ship.moving_left:
            # Ship hasn't started moving yet; move to the right.
            ship.moving_right = True
        elif (ship.moving_right
                    and ship.rect.right > screen_rect.right - 10):
            # Ship about to hit right edge; move left.
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            ship.moving_left = False
            ship.moving_right = True

    def _modify_speed(self, speed_factor):
        --snip--
```

First we create an attribute called `fleet_size`, which we initialize in `run_game()` before starting the while loop. We need to grab the fleet size before any of the aliens have been shot down.

The method `_control_ship()` would get pretty long, and the if blocks would be nested deeper than we'd like if we left all of the ship movement logic in this one method. So we move all the sweeping left and right logic to a new method called `_sweep_left_right()`. In `_control_ship()`, we call `_sweep_left_right()` as long as the current fleet size, `len(self.ai_game.aliens)` is greater than half of the original fleet size. When half of the fleet has been destroyed, we stop the ship's movement and no longer call `_sweep_left_right()`.

This is not an improvement on the basic sweeping strategy, but it does show you how to transition from one strategy to another as your automated player makes progress within a level. You could implement a new strategy when there's just one or two aliens left, or even have a series of strategies for increasingly specific situations.

In the last section, we'll look at how you can pick out a specific alien and target that individual alien.

[top](#top)

### Targeting a specific alien

At some point you'll probably want to target a specific alien. You can develop some interesting strategies and game play by targeting specific aliens, or groups of aliens. In this section, I'll show you one such strategy and leave you to implement more effective strategies.

In this approach we'll always target the right-most alien in the bottom row. We'll pick that alien from the group of aliens, and then always move the ship towards that alien. All of the code to do this goes in `_control_ship()`, and a new method called `_get_target_alien()`:

```python
    def _control_ship(self):
        """Controls automated movement of the ship."""

        # Get specific alien to chase.
        target_alien = self._get_target_alien()

        # Move toward target alien.
        ship = self.ai_game.ship
        if ship.rect.x < target_alien.rect.x:
            ship.moving_right = True
            ship.moving_left = False
        elif ship.rect.x > target_alien.rect.x:
            ship.moving_right = False
            ship.moving_left = True

    def _get_target_alien(self):
        """Get a specific alien to target."""
        # Find the right-most alien in the bottom row.
        #   Pick the first alien in the group. Then compare all others, 
        #   and return the alien with the greatest x and y rect attributes.
        target_alien = self.ai_game.aliens.sprites()[0]
        for alien in self.ai_game.aliens.sprites():
            if alien.rect.y > target_alien.rect.y:
                # This alien is farther down than target_alien.
                target_alien = alien
            elif alien.rect.y < target_alien.rect.y:
                # This alien is above target_alien.
                continue
            elif alien.rect.x > target_alien.rect.x:
                # This alien is in the same row, but farther right.
                target_alien = alien
        
        return target_alien
```

In `_control_ship()`, we remove the call to `_sweep_left_right()`. We keep that method in the class, because we might want to use it in another strategy, but we remove the call to that method.

Let's look at `_get_target_alien()`, because that's the first call we make in `_control_ship()`. We want to pick out the alien that's farthest on the right in the bottom row. There are number of ways to do this, and the approach I use here is not necessarily the best or most efficient approach. When writing for a wide audience, I usually choose an approach that's likely to be clear to many people over a more efficient approach that might be confusing to many people. If you know a more efficient approach to pick out the target alien, feel free to implement that approach.

Remember that a Pygame group is similar to a list, but it's not an actual list. The elements in a group are not kept in a specific order, so you can't grab an element by using an index. The `sprites()` method puts the elements of the group into a list, but not in a predictable order. In `_get_target_alien()` we use `sprites()` to put the aliens in a list so we can grab an individual alien. Then we cycle through all the aliens in the list. If an alien is farther down the screen than `target_alien`, we assign the current alien to `target_alien`. If the alien is farther up the screen, we ignore this alien and continue the loop. Otherwise the alien is in the same row as `target_alien`, and we choose this alien if it's farther to the right than `target_alien`. 

This if block was a little tricky to write; I didn't get it right the first time. My first attempt examined x and y at the same time, and ended up chasing aliens that were farther up the screen but also farther right than the rightmost alien in the bottom row. This is actually an interesting strategy, because it makes it harder for the fleet to descend. You might try implementing a strategy that aims at clearing the fleet one column at a time, starting from one of the edges.

Once we have a target alien selected, we can position the ship. Back in `_control_ship()`, if the ship is to the left of the target alien we start moving right. If the ship is to the right of the target alien, we move left.

When you run this code, you'll see that matching an alien's position exactly doesn't work all that well, because by the time the bullet reaches the alien's vertical position, the alien has moved away. The ship ends up chasing aliens until they're so low they can't get away. This is a case where introducing a bit of randomness into the firing can be effective. You can also explore strategies for targeting aliens, but not staying right underneath them. It's an interesting geometry exercise to try and work out how to make a bullet hit the desired alien every time. But if that's not your strong suit, there are plenty of ways to get near enough to specific aliens that you can reliably shoot them down. If you don't want to try working out an exact solution to hitting aliens, you can try adding some randomness to the ship's position as well. I imagine the right amount of randomness might cause the ship to end up in the right position often enough to hit the alien without getting into long stretches of alway firing behind the alien's position. You might also try stopping, and firing when the alien is a certain distance away to see if that results in a higher level of accuracy. There are lots of approaches you can try implementing, even if you can't work out the mathematically optimal approach. And many of these strategies are really interesting to watch at higher speeds.

I also want to point out that I haven't optimized any of this code. I'm writing this guide to show people how you can start to automate the game play in Alien Invasion, and this is representative of how I approach some of my development work. Often times in exploratory work I jot a sentence or two about what I'm trying to do, then write some code to see how that idea works. Then if I like that approach but I'm not going to do anything more with it, I leave the unoptimized code in place. If I'm going to build on that code, I spend some more time thinking about how to make the code more efficient. Here, for example, we're looping through the list of aliens on every game cycle. That's really inefficient! But it doesn't appear to affect the game's performance, so I'm not too worried about it at the moment. If I was building on this project, I'd make the target alien an attribute of the class, and then only call `_get_target_alien()` if target alien does not exist, which should happen every time the target alien is destroyed. The loop would never run more than once per the number of aliens on the screen. If you are curious about this, try to implement this approach. You can code a counter to see how many times `_get_target_alien()` is called in the course of a game, and find out if your optimization made a difference or not.

Sometimes, especially on a larger project or a project that I'm doing for someone else, I will plan out my overall approach much more carefully and build in some optimization from the beginning.

[top](#top)

## Closing Thoughts

If you are getting into this project, you might want to implement a more refined approach to tracking statistics in the game. You can track hits and misses, and report a hit/miss ratio. Then you can compare different strategies not just on the high scores or completed levels they achieve, but on how efficiently they perform as well.

Hopefully this guide helps you get started automating the game play in Alien Invasion. If you come up with an effective or interesting strategy, please share it! You can tag your solution with [#ai_player](https://twitter.com/hashtag/ai_player) on Twitter, or send it to me through email (ehmatthes at gmail). Good luck, and if this doesn't work for you please let me know as well.

[top](#top)