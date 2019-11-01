---
layout: default
title: Playing Cards
parent: Challenges
nav_order: 5
---

# Challenges - Playing Cards
{: .no_toc }

In this investigation, you'll start out by modeling a deck of playing cards. You'll then write a set of functions or classes that let you work with your deck. You'll write code that lets you play one or more card games against the computer, at varying levels of difficulty. You can then choose to make a graphical card game, analyze the results of playing the games many times, or build a web app that lets you play the game.

You do not have to do every challenge in the set. If a challenge depends on completing another set, that is indicated in the challenge. Challenges are grouped by chapter, so you'll know when you can start on each challenge.

* 
{:toc}

---

## Chapter 3

### Challenge 3-1: Hearts

Make a list of all the cards in a deck of cards that have hearts on them. Your list would have items like '2 of Hearts', '3 of Hearts', '4 of Hearts', etc. Print 3 of your cards.

---

## Chapter 4

### Challenge 4-2: Heart Loops

Make a list of all the cards in a deck of cards that have hearts on them. Your list would have items like '2 of Hearts', '3 of Hearts', '4 of Hearts'. Do this efficiently by using a loop to generate as many cards as you can.

- Loop through your list and print out all of the cards in order.
- Loop through a slice of your list and print out just the cards with numbers on them.
- Loop through a slice of your list and print out just the face cards.

### Challenge 4-3: Full Deck

Expand on *Hearts* to generate a list containing every card in a standard deck of cards. Using loops to generate some of the cards, how efficiently can you do this?

---

## Chapter 8

### Challenge 8-1: Basic Card Functions

To do this challenge, you first need to do Challenge 4-3, *Full Deck*. Write a series of functions that help you work with cards from your deck:

- Write a function called `get_suit()`. This function takes one card as an argument, and returns the suit of that card.
- Write a function called `get_value()`. This function takes one card as an argument, and returns the value of the card. The value of a face card would be 'J' or 'Jack', 'Q' or 'Queen', and so forth.
- Write a function called `same_value()`. This function takes two cards, and returns `True` if the cards have the same value, and `False` if they do not.
  - Extension: Write this function so that it works for two or more cards.
- Write a function called `same_suit()`. This function takes two cards, and returns `True` if the cards have the same suit, and `False` if they do not.
  - Extension: Write this function so that it works for two or more cards.

### Challenge 8-2: Basic Deck Functions

You should do challenge 8-1, *Basic Card Functions* before trying this challenge. Write a series of functions that work with a whole deck:

- Write a function called `build_deck()`. This function takes no arguments, and returns a list containing all the cards in a standard deck, in order.
- Write a function called `deal_top_card()`. This function accepts a deck as an argument, and returns the first card in the deck. It also removes that card from the deck.
- Write a function called `get_random_card()`. This function accepts a deck as an argument, and returns a random card from the deck. It also removes that card from the deck.
- Write a function called `shuffle_deck()`. This function accepts a deck as an argument, and randomizes the order of the deck.
- Write a function called `deal_hand()`. This function accepts a deck as an argument, and the size of the hand. The function returns a list containing the cards in the hand. The function also removes these cards from the deck.
    - Extra challenge: This function should more properly be called `deal_hands()`. It should accept three arguments - the deck, the number of hands to deal, and the size of the hand. It should return a list of hands. This is more complicated, so consider taking the simplified route of just writing `deal_hand()`, and call it sequentially when you need to generate a number of hands.

### Challenge 8-3: Go Fish

You should do challenges 8-1 and 8-2, *Basic Card Functions* and *Basic Deck Functions*, before trying this challenge. After completing these two challenges you have everything you need to code a game of Go Fish that you can play against the computer!

### Challenge 8-4: AI Go Fish

You need to do Challenge 8-3, *Go Fish*, before trying this challenge. If the computer player in your Go Fish game makes moves by randomly choosing a card in its hand to ask you about, you have a very weak Go Fish player. Consider a strategy for playing Go Fish well, and implement that strategy in code. For example, a good Go Fish player remembers when the other player has asked about a card. Your computer player should do this as well!

---

## Chapter 9

### Challenge 9-1: Deck of Cards

Write code to represent a deck of cards. Your code should contain all the functionality described in Challenges 8-1 and 8-2, *Basic Card Functions* and *Basic Deck Functions*. To recap, that includes the following functions or methods:

- Card-focused functionality
    - `get_suit()`
    - `get_value()`
    - `same_value()`
    - `same_suit()`
- Deck-focused functionality
    - `build_deck()`
    - `get_first_card()`
    - `get_random_card()`
    - `shuffle_deck()`
    - `deal_hand()`

### Challenge 9-2: Go Fish

Use your class-based deck of cards to implement a game of Go Fish that you can play against the computer.

### Challenge 9-3: Scoring Go Fish

Report the number of cards in the player's hand, and the computer's hand. Report the number of turns that have been played.

---

## Chapter 10

### Challenge 10-1: Statistics

For your Go Fish game, create a file that tracks statistics for the game. Keep track of wins and losses, even when the game is not running.

---

## Chapter 11

### Challenge 11-1: Testing Your Deck

Pass

### Challenge 11-2: Testing Go Fish

Pass