# Write a program to find the largest number in a list.
def findLargestNumber(numbers):
    if not numbers:
        return None
    maxNumber = list[0]
    for number in list:
        if number > maxNumber:
            maxNumber = number
    return maxNumber

numbers = []
print('Max Number in list is: ' + str(findLargestNumber(numbers)))                    