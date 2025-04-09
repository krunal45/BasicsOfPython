# **Question**: Write a Python program that asks the user to input a number and then prints "Even" if
# the number is even (divisible by 2) or "Odd" if the number is odd.
number = int(input('Please enter number: '))
if number %2 == 0:
    print('Even')
else:
    print('Odd')