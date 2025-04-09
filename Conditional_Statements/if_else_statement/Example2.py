# **Question**: Write a Python program that asks the user to input a number and then prints whether 
# the number is "Positive" (greater than 0) or "Negative or Zero" (less than or equal to 0).
number = int(input('Please Enter Number: '))
if number <= 0:
    print('Negative or Zero')
else:
    print('Positive')