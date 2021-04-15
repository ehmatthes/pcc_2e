---
layout: default
title: Chapter 12
parent: Solutions
nav_order: 102
---

# Solutions - Chapter 12
{: .no_toc }

There are a few things that can be helpful to know as you work on the exercises for Chapters 12-14:
- The solutions for Chapters 12-14 are kept in a [separate repository](https://github.com/ehmatthes/pcc_2e_ai_solutions), because every exercise is a mini project. These pages contain links to individual solutions in the repository.
- If you make a mistake when working through the project and can't get it back to a working state, it can be really frustrating to start over from scratch. There are some resources that can help with this:
  - In the [online resources](https://github.com/ehmatthes/pcc_2e), there's a complete version of the Alien Invasion project as it looks at the end of each main section in Chapters 12-14.
  - For example if you're working on getting the ship to move and everything stops working, you can look at the [versions from Chapter 12](https://github.com/ehmatthes/pcc_2e/tree/master/chapter_12), then click on the [adding_ship_image](https://github.com/ehmatthes/pcc_2e/tree/master/chapter_12/adding_ship_image) folder, and you'll have a working copy of the project as it looks at the beginning of the section about making the ship move.
  - If you want to compare your files to what they should look like at the end of the Piloting the Ship section, click on the [piloting_the_ship](https://github.com/ehmatthes/pcc_2e/tree/master/chapter_12/piloting_the_ship) folder.
  - If you want to know how to make snapshots of a project like this, make time to work through Appendix D, Using Git for Version Control. It will be well worth your time, and it's something you'll use your whole life as a programmer.
- If you haven't already seen the [cheat sheets](../../cheat_sheets/cheat_sheets/), there's a sheet that focuses on Pygame which might be helpful when working on these exercises.
- It can be helpful to look through some of the [Pygame documentation](https://www.pygame.org/docs/) as you work on these exercises. There are also direct links to specific pages in the documentation that are helpful for certain exercises.
- If you're enjoying the Alien Invasion project, make sure to check out the section about [adding sound and automating gameplay](../../beyond_pcc/ai_player/). You can add sounds to the game in about ten lines of code, and if you're interested you can do a bit more work and make an automated player for the game.

---

* 
{:toc}

Back to [solutions](../solutions).

---

## 12-1: Blue Sky

Make a Pygame window with a blue background.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_12/solution_12_1)

## 12-2: Game Character

Find a bitmap image of a game character you like or convert an image to a bitmap. Make a class that draws the character at the center of the screen and match the background color of the image ot the background color of the screen, or vice versa.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_12/solution_12_2)

## 12-4: Rocket

Make a game that begins with a rocket in the center of the screen. Allow the player to move the rocket up, down, left, or right using the four arrow keys. Make sure the rocket never moves beyond any edge of the screen.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_12/solution_12_4)

## 12-5: Keys

Make a Pygame file that creates an empty screen. In the event loop, print the `event.key` attribute whenever a `pygame.KEYDOWN` event is detected. Run the program and press various keys to see how Pygame responds.

Note: *When you're working on this exercise, it can be helpful to look at the [documentation for `pygame.key`](https://www.pygame.org/docs/ref/key.html). Also, if you run the solution code shown here, you'll get the integer code for each key. That is expected, even though we use the constant that's mapped to these values, such as `pygame.K_q` or `pygame.K_SPACE`.*

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_12/solution_12_5)

## 12-6: Sideways Shooter

Write a game that places a ship on the left side of the screen and allows the player to move the ship up and down. Make the ship fire a bullet that travels right across the screen when the player presses the spacebar. Make sure bullets are deleted once they disappear off the screen.

[Solution](https://github.com/ehmatthes/pcc_2e_ai_solutions/tree/main/ch_12/solution_12_6)