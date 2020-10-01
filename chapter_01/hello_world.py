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
# range(start, stop, step)
for i in range(8):
    print(i)
