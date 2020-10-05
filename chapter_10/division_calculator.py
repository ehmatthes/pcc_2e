# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

print('\nGive me 2 numbers; I will divide them.')
print('Enter \'q\' to quit.')

while True:
    num1 = input('\nFirst Number: ')
    if num1 == 'q':
        break
    num2 = input('Second Number: ')
    if num2 == 'q':
        break
    try:
        answer = int(num1) / int(num2)
    except ZeroDivisionError:
        print('Denominator cannot be 0!')
    else:
        print(answer)
        