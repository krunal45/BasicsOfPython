# Write a program to reverse a number and string without using pre-built methods.
def reverseNumber(number):
    result = 0
    while(number!=0):
        digit = number % 10
        result = (result*10) + digit
        number = number // 10
    return result

def reverseString(name):
    name = list(name)
    reverseName = []
    for index in range(len(name)-1,-1,-1):
        reverseName.append(name[index])
    return ''.join(reverseName)
        
number = reverseNumber(123)   
print('Reversed number is > '+str(number))
print('Reversed name > '+reverseString('Krunal'))