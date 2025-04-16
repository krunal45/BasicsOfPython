# Question: Verify if given number is prime or not

def isPrime(number):
    if number < 2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    else:
        return True

number = int(input('Please Enter Number: '))
print(f'is {number} prime ? ',isPrime(number))       