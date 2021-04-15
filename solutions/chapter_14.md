---
layout: default
title: Chapter 14
parent: Solutions
nav_order: 106
---

# Solutions - Chapter 14
{: .no_toc }

The solutions for Chapters 12-14 are kept in a [separate repository](https://github.com/ehmatthes/pcc_2e_ai_solutions), because every exercise is a mini project. This page contains links to individual solutions in the repository.

If you haven't already seen the [cheat sheets](../../cheat_sheets/cheat_sheets/), there's a sheet that focuses on Pygame which you might find helpful when working on these exercises.

Also, it's helpful to have a look through some of the [Pygame documentation](https://www.pygame.org/docs/) as you work on these exercises. There are also direct links to specific pages in the documentation that are helpful for certain exercises.

If you've enjoyed the Alien Invasion project, make sure to check out the section about [adding sound and automating gameplay](../../beyond_pcc/ai_player/). You can add sounds to the game in about ten lines of code, and if you're curious you can do a bit more work and make an automated player for the game.

---

* 
{:toc}

Back to [solutions](../solutions).

---

## 14-1: Press P to Play

Because *Alien Invasion* uses keyboard input to control the ship, it would be useful to start the game with a keypress. Add code that lets the player press P to start. It might help to move some code from `_check_play_button()` to a `_start_game()` method that can be called from `_check_play_button()` and `_check_keydown_events()`.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_14/solution_14_1)

## 14-2: Target Practice

Create a rectangle at the right edge of the screen that moves up and down at a steady rate. Then have a ship appear on the left side of the screen that the player can move up and down while firing bullets at the moving, rectangular target. Add a Play button that starts the game, and when the player misses the target three times, end the game and make the Play button reappear. Let the player restart the game with this Play button.

Note: *This solution uses the `pygame.sprite.spritecollide()` function, which detects whether a single sprite has collided with any member of a group. It might be helpful to look at the [documentation for this function](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollide) before looking at the solution.*

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_14/solution_14_2)

## 14-3: Challenging Target Practice

Start with your work from Exercise 14-2 (page 285). Make the target move faster as the game progresses, and restart the target at the original speed when the player clicks Play.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_14/solution_14_3)

## 14-4: Difficulty Levels

Make a set of buttons for *Alien Invasion* that allows the player to select an appropriate starting difficulty level for the game. Each button should assign the appropriate values for attributes in `Settings` needed to create different difficulty levels.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_14/solution_14_4)

## 14-5: All-Time High Score

The high score is reset every time a player closes and restarts *Alien Invasion*. Fix this by writing the high score to a file before calling `sys.exit()` and reading in the high score when initializing its value in `GameStats`.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_14/solution_14_5)