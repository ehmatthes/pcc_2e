---
layout: default
title: Chapter 8
parent: Challenges
nav_order: 50
---

# Challenges - Chapter 8
{: .no_toc }

* 
{:toc}

---

## Challenge 8-1: Basic Card Functions

To do this challenge, you first need to do Challenge 4-3, *Full Deck*. Write a series of functions that help you work with cards from your deck:

- Write a function called `get_suit()`. This function takes one card as an argument, and returns the suit of that card.
- Write a function called `get_value()`. This function takes one card as an argument, and returns the value of the card. (In many card games, the face cards each have a value of 10 points.)
- Write a function called `same_value()`. This function takes two cards, and returns `True` if the cards have the same value, and `False` if they do not.
  - Extension: Write this function so that it works for two or more cards.
- Write a function called `same_suit()`. This function takes two cards, and returns `True` if the cards have the same suit, and `False` if they do not.
  - Extension: Write this function so that it works for two or more cards.

## Challenge 8-2: Basic Deck Functions

You should do challenge 8-1, *Basic Card Functions* before trying this challenge. Write a series of functions that work with a whole deck:

- Write a function called `build_deck()`. This function takes no arguments, and returns a list containing all the cards in a standard deck, in order.
- Write a function called `get_first_card()`. This function accepts a deck as an argument, and returns the first card in the deck.
- Write a function called `get_random_card()`. This function accepts a deck as an argument, and returns a random card from the deck.
- Write a function called `shuffle_deck()`. This function accepts a deck as an argument, and randomizes the order of the deck.
- Write a function called `deal_hand()`. This function accepts a deck as an argument, and the size of the hand. The function returns a list containing the cards in the hand.

## Challenge 8-3: Go Fish

You should do challenges 8-1 and 8-2, *Basic Card Functions* and *Basic Deck Functions*, before trying this challenge. After completing these two challenges you have everything you need to code a game of Go Fish that you can play against the computer!

## Challenge 8-4: AI Go Fish

You need to do Challenge 8-3, *Go Fish*, before trying this challenge. If the computer player in your Go Fish game makes moves by randomly choosing a card in its hand to ask you about, you have a very weak Go Fish player. Consider a strategy for playing Go Fish well, and implement that strategy in code. For example, a good Go Fish player remembers when the other player has asked about a card. Your computer player should do this as well!