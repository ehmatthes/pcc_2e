---
layout: default
title: Playing Cards
parent: Challenges
nav_order: 20
---

# Challenges - Playing Cards
{: .no_toc }

In this investigation, you'll start out by modeling a deck of playing cards. You'll then write a set of functions or classes that let you work with your deck. You'll write code that lets you play one or more card games against the computer, at varying levels of difficulty. You can then choose to make a graphical card game, analyze the results of playing the games many times, or build a web app that lets you play the game.

You do not have to do every challenge in the set. If a challenge depends on completing another set, that is indicated in the challenge. Challenges are grouped by chapter, so you'll know when you can start on each challenge.

* 
{:toc}

---

## Chapter 3

### Playing Cards 3-1: Hearts

Make a list of all the cards in a deck of cards that have hearts on them. Your list would have items like '2 of Hearts', '3 of Hearts', '4 of Hearts', etc. Print 3 of your cards.

Build your list using the syntax you want to practice. For example, you might consider starting with an empty list and using a series of `append()` or `insert()` calls.

[top](#top)

---

## Chapter 4

### Playing Cards 4-2: Heart Loops

Make a list of all the cards in a deck of cards that have hearts on them. Your list would have items like '2 of Hearts', '3 of Hearts', '4 of Hearts'. Do this efficiently by using a loop to generate as many cards as you can.

- Loop through your list and print out all of the cards in order.
- Loop through a slice of your list and print out just the cards with numbers on them.
- Loop through a slice of your list and print out just the face cards.

### Playing Cards 4-3: Full Deck

Expand on *Hearts* to generate a list containing every card in a standard deck of cards. Using loops to generate some of the cards, how efficiently can you do this?

Print the entire deck. Then choose a suit, and print just the cards in that suit.

*Prerequisite: [Playing Cards 4-2: Heart Loops](#playing-cards-4-2-heart-loops)*

[top](#top)

---

## Chapter 6

### Playing Cards 6-1: Full Deck

Now that you've learned about nested loops, can you write a nested loop that creates an entire deck of cards?

Print the entire deck. Then choose a suit, and print just the cards in that suit.

*Prerequisite: [Playing Cards 4-2: Heart Loops](#playing-cards-4-2-heart-loops)*

---

## Chapter 8

### Playing Cards 8-1: Basic Card Functions

Write a series of functions that help you work with cards from your deck:

- Write a function called `build_deck()`. This function takes no arguments, and returns a list containing all the cards in a standard deck, in order.
- Write a function called `get_suit()`. This function takes one card as an argument, and returns the suit of that card.
- Write a function called `get_value()`. This function takes one card as an argument, and returns the value of the card. The value of a face card would be 'J' or 'Jack', 'Q' or 'Queen', and so forth.
- Write a function called `same_value()`. This function takes two cards, and returns `True` if the cards have the same value, and `False` if they do not.
  - Extension: Write this function so that it works for two or more cards.
- Write a function called `same_suit()`. This function takes two cards, and returns `True` if the cards have the same suit, and `False` if they do not.
  - Extension: Write this function so that it works for two or more cards.

*Prerequisite: [Playing Cards 6-1: Full Deck](#playing-cards-6-1-full-deck)*

### Playing Cards 8-2: Basic Deck Functions

Write a series of functions that work with a whole deck. You might need to see the short [guide to working with the `random` module](../../beyond_pcc/random_functions/) when implementing some of these functions.

- Write a function called `deal_top_card()`. This function accepts a deck as an argument, and returns the first card in the deck. It also removes that card from the deck.
- Write a function called `get_random_card()`. This function accepts a deck as an argument, and returns a random card from the deck. It also removes that card from the deck.
- Write a function called `shuffle_deck()`. This function accepts a deck as an argument, and randomizes the order of the deck.
- Write a function called `deal_hand()`. This function accepts a deck as an argument, and the size of the hand. The function returns a list containing the cards in the hand. The function also removes these cards from the deck.
    - Extra challenge: This function should more properly be called `deal_hands()`. It should accept three arguments - the deck, the number of hands to deal, and the size of the hand. It should return a list of hands. This is more complicated, so consider taking the simplified route of just writing `deal_hand()`, and call it sequentially when you need to generate a number of hands.

*Prerequisite: [Playing Cards 8-1: Basic Card Functions](#playing-cards-8-1-basic-card-functions)*

### Playing Cards 8-3: Go Fish

Implement a game of Go Fish that you can play against the computer. A basic Go Fish game has the following rules:

- Each player is dealt a hand of 7 cards.
- If either player has a pair, they pull the pair from their hands and place them on the table.
- One player goes first. The player picks a card in their hand that they're trying to match, and they say, "Do you have a Jack?"
  - If the other player has a Jack, the asking player gets that card and places both Jacks on the table. The asking player goes again.
  - If the other player doesn't have a Jack, they say "Go Fish!" The asking player draws a card from the deck and puts it in their hand.
    - If the drawn card is the card they asked for, they place the pair on the table and go again.
    - If the drawn card matches any other card in their hand, they place the pair on the table but don't go again.
- The game is over whenever one player runs out of cards.
- The player with the most pairs at the end of the game wins, regardless of who ran out of cards first.

*Note: There are a number of variations to Go Fish. Feel free to make any variations you need to the above rules to match your style of play.*

*Prerequisite: [Playing Cards 8-2: Basic Deck Functions](#playing-cards-8-2-basic-deck-functions)*

### Playing Cards 8-4: AI Go Fish

If the computer player in your Go Fish game makes moves by randomly choosing a card in its hand to ask you about, you have a very weak Go Fish player. Consider a strategy for playing Go Fish well, and implement that strategy in code. For example, a good Go Fish player remembers when the other player has asked about a card. Your computer player should do this as well!

*Prerequisite: [Playing Cards 8-3: Go Fish](#playing-cards-8-3-go-fish)*

[top](#top)

---

## Chapter 9

### Playing Cards 9-1: Deck of Cards

Write a class, or set of classes, to represent a deck of cards. Your code should contain all the functionality described in Challenges 8-1 and 8-2, *[Basic Card Functions](#playing-cards-8-1-basic-card-functions)* and *[Basic Deck Functions](#playing-cards-8-2-basic-deck-functions)*. To recap, that includes the following functions or methods:

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

*Prerequisites: There are no prerequisites for this challenge. If you haven't done the previous card-related challenges, and you want to jump in here, go ahead. If the class-based version of this challenge is too difficult, consider trying some of the earlier challenges in this series.*    

### Playing Cards 9-2: Go Fish

Use your class-based deck of cards to implement a game of Go Fish that you can play against the computer. A basic Go Fish game has the following rules:

- Each player is dealt a hand of 7 cards.
- If either player has a pair, they pull the pair from their hands and place them on the table.
- One player goes first. The player picks a card in their hand that they're trying to match, and they say, "Do you have a Jack?"
  - If the other player has a Jack, the asking player gets that card and places both Jacks on the table. The asking player goes again.
  - If the other player doesn't have a Jack, they say "Go Fish!" The asking player draws a card from the deck and puts it in their hand.
    - If the drawn card is the card they asked for, they place the pair on the table and go again.
    - If the drawn card matches any other card in their hand, they place the pair on the table but don't go again.
- The game is over whenever one player runs out of cards.
- The player with the most pairs at the end of the game wins, regardless of who ran out of cards first.

*Note: There are a number of variations to Go Fish. Feel free to make any variations you need to the above rules to match your style of play.*

*Prerequisite: [Playing Cards 9-1: Deck of Cards](#playing-cards-9-1-deck-of-cards)*

### Playing Cards 9-3: Scoring Go Fish

Report the number of cards in the player's hand, and the computer's hand. Report the number of turns that have been played. Keep track of the pairs that each player has won, and display the number of pairs won by each player.

*Prerequisite: [Playing Cards 9-2: Go Fish](#playing-cards-9-2-go-fish)*

### Playing Cards 9-4: AI Go Fish

If the computer player in your Go Fish game makes moves by randomly choosing a card in its hand to ask you about, you have a very weak Go Fish player. Consider a strategy for playing Go Fish well, and implement that strategy in code. For example, a good Go Fish player remembers when the other player has asked about a card. Your computer player should do this as well!

Extension: Write a version of this game where the computer plays itself.

*Prerequisite: [Playing Cards 9-2: Go Fish](#playing-cards-9-2-go-fish) It will probably also be helpful to complete [Playing Cards 9-3: Scoring Go Fish](#playing-cards-9-3-scoring-go-fish) as well.*

### Playing Cards 9-5: Other Card Games

Consider other card-based games you know such as Poker, Solitaire, War, Rummy, Crazy Eights, and others. Implement one of these games so that you can play it against the computer.

*Note: Many card-based games are much easier to work on in a graphical environment. For example, it's much easier to examine a poker hand when you can see the colors of the cards in your hand. If the game you're working on is getting difficult because of the text-based terminal interface, you might want to work through Chapters 12-14 and then implement the game using Pygame.*

*That said, it can be easier to work on some of the game logic outside the complexity of a graphical framework. So if you're enjoying working on card games and don't want to wait until after Chapter 14, go ahead and get started on the game you're interested in.*

[top](#top)

---

## Chapter 10

### Playing Cards 10-1: Statistics

Create a file that tracks statistics for the card game you've implemented. Keep track of wins and losses, and update the statistics after each completed game. You may choose to keep track of just wins and losses, or more detailed information such as how many turns were played, how many pairs each player ended with, and how many cards the losing player was left holding. Display the overall statistics at the start of the game, and after each game has finished.

*Prereqisite: Any of the challenges where you have implemented a card game that you can play against the computer.*

[top](#top)

---

## Chapter 11

### Playing Cards 11-1: Testing Your Deck

Write some tests for the deck functions or classes that you've written. You might start with any or all of the following tests:

- Test that a newly-built deck has the correct number of cards in it.
- Test that a newly-built deck has the correct number of 2s, 3s, 4s, etc.
- Write a full deck to a file. Build a new deck, and test that your new deck matches the deck you've saved in a file.
- Build a new deck, and deal some cards. Test that the cards that should have been dealt were actually dealt. Test that the remaining deck is the size it should be.

*Prerequisites: Any of the card or deck functions or classes you've written, such as [Playing Cards 8-2: Basic Deck Functions](#playing-cards-8-2-basic-deck-functions) or [Playing Cards 9-1: Deck of Cards](#playing-cards-9-1-deck-of-cards).*

### Playing Cards 11-2: Testing Go Fish

Write some tests for your game. Consider any or all of the following:

- Build non-random hands for each player. Test that a correct guess is processed correctly, and that an incorrect guess is processed correctly. Make sure you test the processing of the user's guesses, and the computer's guesses.
- Build a hand for each player that has one or two pairs in it. Test that these pairs are pulled from the hands before the first turn happens.
- Write a test ensuring that when either player draws a card that matches another card in their hand, that pair is pulled before the next turn.

*Prerequisites: A Go Fish game, such as [Playing Cards 8-3: Go Fish](#playing-cards-8-3-go-fish) or [Playing Cards 9-2: Go Fish](#playing-cards-9-2-go-fish).*

[top](#top)

---

## Chapter 14

### Playing Cards 14-1: Go Fish Game

PyGame is a great framework for building a graphical version of Go Fish. You can find a set of card images [here](https://pixabay.com/vectors/card-deck-deck-cards-playing-cards-161536/). You can also find this file as *playing_cards.bmp* in the *beyond_pcc* folder in the zip file of online resources for the book.  

In your Go Fish game, the player should see all the cards in their hand once the game begins. They should see a card back for each card in the computer's hand, and a set of cards representing the draw pile. They should be able to click on a button to ask for a certain card. If they are incorrect, they should have to click on the draw pile to draw their card. They should see their card, and if they got what they asked for they should get to go again. When their turn is completely over, they should click a button to let the computer take its turn.

Start with a basic version of the game, and then implement a scoring system.

*Prerequisites: A Go Fish game, such as [Playing Cards 9-2: Go Fish](#playing-cards-9-2-go-fish).*

[top](#top)

---

## Chapter 15

### Playing Cards 15-1: Go Fish Statistics - Visualized

Create a Go Fish game, in which the computer follows a specific strategy. Make a version of the game where the computer plays itself. Write a loop of some sort that makes the computer play itself 100 times or more.

Develop several questions about what might happen over the course of a large number of Go Fish games, such as:

- At the end of each game, how many cards was each player holding?
- How many games does each player win?
- How often does one player end up with all the cards?

Make a guess about what you think the answers to these questions might be. Then make a visualization, or series of visualizations, that answer these questions based on your simulated game play.

*Prerequisites: A Go Fish game, such as [Playing Cards 9-2: Go Fish](#playing-cards-9-2-go-fish).*

[top](#top)

---

## Chapter 20

### Playing Cards 20-1: Go Fish Online

Develop an online version of Go Fish. This could be text-based, or it could be image based.

*Prerequisites: A Go Fish game, such as [Playing Cards 9-2: Go Fish](#playing-cards-9-2-go-fish).*