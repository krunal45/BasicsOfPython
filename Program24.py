# W.a.p to find prime numbers from list of numbers.
numbers = [1, 3, 4, 5, 6]

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2 or number == 3:
        return True  # 2 and 3 are prime
    if number % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    for i in range(3, int(number ** 0.5) + 1, 2):  # Check only odd numbers up to sqrt(number)
        if number % i == 0:
            return False
    return True

# Function to get prime numbers from a list
def getPrimeNumbers(numbers):
    primeNumbers = []
    for number in numbers:
        if is_prime(number):
            primeNumbers.append(number)
    return primeNumbers

# Print the list of prime numbers
print(getPrimeNumbers(numbers))