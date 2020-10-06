# message = "Hello Python world!"

# print (message)

# message = "New message."

# print(message)

# print(type(2+5))

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
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

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
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

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### Tuple
# Order is preserved
# patient1_data = ("Pippa", "Luigi", 7, "cat")
# print (patient1_data[2])

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
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

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
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

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
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

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
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

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
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

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
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

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### Strings (are immutable)
# s = 'foo'
# t = 'bar'
# u = 'baz'

# print(s+t)
# print(s+t+u)
# print(s*4)
# print(u*-1) # output: ''
# print('foobar' * -2) # output: ''
# s in 'That\'s food for thought' # output: True
# s not in 'That\'s good for thought' # output: True

# int() # str --> int
# chr() # int --> character
# ord() # character --> int
# len() # returns length
# str() # stringify

# all info stored as nums. ord() returns ASCII
# ord('a') #output: 97

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### String Indexing
# s = 'timbucktoo'
# s[4] #output: 'u'
# s[-3] #output: 't'

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### String Slicing, inclusive of first, exclusive of last index
# s = 'excoriate'
# s[2:5] #output: 'cor'
# s[:4] # 'exco'
# s[2:] # 'coriate'
# s[:n] + s[n:] = s # true if 0 <oreq n <oreq len(s)
# s[2:2] # ''
# s[4:2] # ''
# s[-5:-2] == s[1:4] # true

## Adding a third index designates a stride (also called a step)
# s = 'excoriate'
# s[0:9:2] # 'ecrae'

# s = '12345' * 5 # '1234512345123451234512345'
# s[::5] # '11111'

# s = 'foobar'
# s[5:0:-2] # 'rbo'

## Reverse a string in Python
# s = 'If Comrade Napoleon says it, it must be right.'
# s[::-1] # '.thgir eb tsum ti ,ti syas noelopaN edarmoC fI'

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### f-string aka Formatted String Literal
# no more crappy concatination
# var = 'Bark'
# print(f'A dog says {var}!')
# print(f'''A dog says {var}!''')

"""
i need to leave a really long comment
i need to leave a really long comment
i need to leave a really long comment
i need to leave a really long comment
"""

# var = 'James'
# print(f'{var} is sexy')

### f strings
# s='f-strings aka Formatted String Literal and super dope'
# s[0:4]
# s[::3]
# s.upper()
# s.lower().count('s') #4
# s.lower().count('s', 0, 20) #2

# 'foobar'.endswith('bar') #True

# # Returns the lowest index in s where substring <sub> is found.
# s.find('aka') #10 if sub not found, returns -1
# s.index('aka', 11) # ValueError: substring not found

# try:
#     answer = s.index('aka', 11)
# except ValueError:
#     print('Substring \'aka\' it not a part of the original string.')
# else:
#     print(answer)

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### Exception Obj and Error Handling

# No Error Handling
# result = 5/0
# print(result)

# Yes Error Handling
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('The denominator cannot be 0. Try again.')

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
# stars = ['Sol', 'Alpha Centauri', 'Bernard', 'Wolf 369']
# print(stars[3])

# peaks_on_plates = {
#     'African':'Kilimanjaro',
#     'Antarctic':'Vinson',
#     'Australian':'Puncak Jaya',
#     'Eurasian':'Everest',
#     'North_America':'Denali',
#     'Pacific':'Mauna Kea',
#     'South_America':'Aconcagua'
# }

# print(peaks_on_plates['Pacific'])

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### Iteration/Loop over a collection
# for i in stars:
#     print(i)
# print('This is executed after the for loop is complete. \nNotice the lack of indentation.')

### Iterate until task complete
# print('Count to 100 by 5\'s')
# i = 5     #iterator
# while i <= 100: 
#     print(i)
#     i += 5
# print('The task is complete.')

### Print the names of fruits in the 
# fruits = ['apples', 'bananas', 'dragon fruits', 'mangoes', 'nectarines', 'pears']

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# i = 1
# while i <= 5:
#     mySum = i
#     mySum = mySum + i
#     i +=1

# print(mySum)

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### Modules
# import testmodule

# testmodule.mult(10, 5)

### -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=
### modules ---> Package or library (set of tools, use as wish) ---> FRAMEWORK (how you accomplish task)
## Framework: some decisions are made for you. Make sure you undersand how to code within the framework.
## Frameworks (Django, Flask)
# OR Use 1+ libraries in your App (ex: TensorFlow, pandas, NumPy, SciPy)
