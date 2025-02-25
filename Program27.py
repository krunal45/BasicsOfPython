### Question:
# Write a Python program that takes a list of numbers and prints only the **odd numbers** from that list
#  using a `for` loop.

def printOddNumbers(list):
    for number in list:
        if number % 2!=0:
            print(number)

printOddNumbers(list=[1,2,4,3,5,6,7,8,9,11,13])