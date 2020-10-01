# message = "Hello Python world!"

# print (message)

# message = "New fucky message."

# print(message)

# print(type(2+5))

### function
# def greeting():
#     name = input("what is your name? ")
#     time = input("what time is it? ")
#     print("Hi" + name + ". It is " + time) 

# greeting()

###  Built in functions
# print(2000 + 3423)
# input("Prompt")

###  Create functions
# def sum(num1, num2):
#     sum = (num1 + num2)
#     print(sum)

# num1 = int(input("what is the first number? "))
# num2 = int(input ("What is the second number? "))
# sum(num1, num2)

### More Functions
# def square(x):
#     return x * x

# result = square(5)
# print(result)


# def sumOfSquares(x, y):
#     squarex = x * x
#     squarey = y * y
#     return squarex + squarey
 

# print(sumOfSquares(4, 10))

### Module - Calendar
# import calendar

# cal = calendar.month(2020, 9)
# print(cal)

### Module - Math
# import math

# squareRoot = math.sqrt(49)
# print(squareRoot)

### Module - Random
# import random

# num = random.randint(1, 100)
# print(num)

# movies = ["movie1", "movie2", "movie3"]
# watch = random.choice(movies)
# print(watch)

# deck = ["Ace", "King", "Queen", "Jack", "10", "9", "8"]
# random.shuffle(deck) 
# print(deck) # original deck is shuffled, but the var is not reassigned

### Tuple
# patient1_data = ("Pippa", "Luigi", 7, "cat")
# print (patient1_data[2])

### Conditionals
# raining = input("Is it raining today? ")
# if raining == "yes":
#     print("Remember your umbrella!")
# else:
#     print("Nice, go outside, ya bitch")

# def minimum(x, y):
#     if x < y:
#         return x
#     else:
#         return y

# print(minimum(8, 2))
# print(minimum(-3, -10))

# raining = input("Is it raining outside? ")
# hasUmbrella = input("Do you have an umbrella? ")
# if raining == "yes" and hasUmbrella == "yes":
#     print("Use your umbrella")
# elif raining == "yes" and hasUmbrella == "no":
#     print("Go get an umbrella from a friend")
# else:
#     print("Outside you go.")

### Foor Loop - Vowels
# word = "excorite" # to critize harshly
# vowels = ["a", "e", "i", "o", "u"]

# vowel_count = 0

# for char in word:
#     if char in vowels:
#         vowel_count += 1

# print(vowel_count)
# list = [3, 6, 8, 3]
# for i in list:
#     print(i)

### For Loop - Range()
# range(start, stop, step) built-in function
# for i in range(8): #stop required, exclusive. Here there will be 8 iterations (0, ..., 7)
#     print(i)

## Print all mulitples of 3 between 4 and 40, inclusive
# for i in range (3, 41, 3):
#     print(i)

# # iterate over the squence
# vowels = ["a", "e", "i", "o", "u"]
# for i in vowels:
#     print(i)

### While Loop - Len()
## Len() input: squence. output: length of sequence
# vowels = ["a", "e", "i", "o", "u"]
# length = len(vowels)
# print(length) 
# # output: 5 
 
# i = 0
# while i < len(vowels):
#     print(vowels[i])
#     i += 1
# # output: 
# # a 
# # e 
# # i 
# # o 
# # u

### Combine module and while loop
# import random

# cats = ["Pip", "O.G. Snagga", "Butters", "Looney Tunes"]
# i = 0
# while i < len(cats):
#     print(cats[i])
#     i += 1
 
# random.shuffle(cats)
# print(cats)

### Recursion
# definition: defining something in terms of itself to achieve your objective.
# A function is recursive if the body of the function calls the function itself. 
# Recursion solves a problem by dividing the problem into smaller subproblems and calling the function itself to solve to solve each subproblem
# Example: Factorial

## Recurision - Factorial of 'n'
# # n! = n(n-1)!

# #  Return the Factorial of a positive int
# def factorial(n):
#     if n == 1:     # Base Case -- simple
#         return 1
#     else:
#         return n * factorial(n-1)

# factorial(5)

# # input | output
# #   5   |   5 * factorial(4) -- 120
# #   4   |   4 * factorial(3) -- 24
# #   3   |   3 * factorial(2) -- 6
# #   2   |   2 * factorial(1)   -- 2
# #   1   |   1

### Sum the digits of a num
# # 125 = 1 + 2 + 5 = 8

# def sum_digits(n):
#     if n < 10:
#         return n
#     else:
#         all_but_last = n // 10
#         last = n % 10
#         return sum_digits(all_but_last) + last

# # input | output
# #   12  |   sum_of_digits(1) + 2  
# #   1   |   1 

### Classes
# class Dog():
#     def __init__(self, name, age):   #self is bound to the Dog object
#         self.name = name # data attribute
#         self.age = age
        
#     def bark(self):
#         print("Woof, woof!")   # method, all get self

# # instantiate class
# Uno = Dog("Uno", 2)
# print(Uno.name)
# Uno.bark()

# Uno.age += 1
# print(Uno.age)

# class Cat():
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#     def is_stinky(self):
#         print("That cat is stinky.")

# Waluigi = Cat("Waluigi", 7, "black/gray striped")
# print(Waluigi.name)
# Waluigi.is_stinky()

