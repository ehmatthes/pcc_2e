---
layout: default
title: Beyond PCC
nav_order: 80
has_children: true
---

# Beyond Python Crash Course
{: .no_toc }

One of the guiding questions for Python Crash Course is, "What's the least you need to know in order to start working on interesting projects?" That's what has helped this book bring people with no programming background to the point where they can understand how to build a meaningful game, make interesting visualizations, and deploy a functioning web app, without it becoming a 1500-page doorstop.

However, once you've understood the material in Python Crash Course, there's a lot more that you're ready to learn. I may write a followup book at some point, but I've also been wanting to write up a series of articles for people who have wanted a little more detail after reading through the book.

Some of this material is just meant to expand your awareness of the fundamentals of programming in general, and Python specifically. Some of this is written to support people working on some of the Challenges, which require specific concepts that weren't included in the book.

If you have questions or feedback about anything presented here, please feel free to [get in touch](/).

Enjoy!

* 
{:toc}

---

- ## [Random Functions](../random_functions/)

    Randomness is discussed when it's needed in the book, but it can be helpful to have a number of these functions described in one place. There are also a couple functions mentioned here that are not covered in the book, which can be useful in some of the challenges.

    *This section will make sense after you've worked through Chapter 4.*


- ## [Using Sprite Sheets in Pygame](../pygame_sprite_sheets/)

    This guide will help you build games that involve lots of images. For example, a deck of cards has 52 different cards in it. If you tried to load 52 separate images, the performance of your game would suffer. Sprite sheets allow you to load one image, and then create game elements from all of the images contained within that single larger image.

    *This section will make sense after you've worked through Chapters 12-14.*

- ## [Pygame: Adding Sound and Automating Game Play](../ai_player/)

    Adding sound to your games makes them much more interesting, and it doesn't take much code. Also, the class-based structure of the Alien Invasion project makes it possible to automate the game play, which is a really interesting exercise.

    *This section will make sense after you've worked through Chapter 14.*

- ## [Pillow: Working with Images](../pillow/)

    Pillow is an imaging library that lets you load and work with existing images, and also lets you create images from a blank canvas. This guide is used for the set of challenges about [making your own photo filters](../../challenges/photo_filters/).

    *This section will make sense after you've worked through Chapter 10.*
