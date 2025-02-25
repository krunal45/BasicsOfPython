# Write a Python program using a while loop that asks the user to input a number. 
# The program should keep running until the user enters the number 0. When 0 is entered, print "Program terminated."
def inputNumber():
    i = None
    while i != 0:
        try:
            i = int(input('Enter Number: (Enter 0 to exit the program!)'))
        except:
            print('Invalid input! Please Enter valid integer!')    
    print('Program terminated.')
inputNumber()        