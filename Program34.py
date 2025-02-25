def findSecondLargestNumber(numbers):
    if(len(numbers)<2):
        return None
    if not areAllNumbersEqual(numbers):
        numbers.sort()
        unique_Numbers = []
        for number in numbers:
            if number not in unique_Numbers:
                unique_Numbers.append(number)
        return unique_Numbers[len(unique_Numbers)-2]
    else:
        return None


def areAllNumbersEqual(numbers):
    return len(set(numbers)) == 1 

number = findSecondLargestNumber(numbers=[2,1,5,98,-30])
print('Second largest number is > '+str(number))

# Code from chat-GPT
# def findSecondLargestNumber(numbers):
#     # Remove duplicates using a set
#     unique_numbers = list(set(numbers))

#     # If there are less than two unique numbers, return None
#     if len(unique_numbers) < 2:
#         return None

#     # Find the two largest numbers
#     unique_numbers.sort()  # Sorting is still needed to get the second largest
#     return unique_numbers[-2]  # Return the second-to-last number (second largest)

# number = findSecondLargestNumber(numbers=[2, 1, 5, 98, -30])
# print('Second largest number is > ' + str(number))