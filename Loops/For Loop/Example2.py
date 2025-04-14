# **Question:**

# Write a Python function called `sum_of_even_indices` that takes a list of numbers as input. 
# The function should iterate through the list using a `for` loop and calculate the sum of only 
# the numbers that are located at even indices (0, 2, 4, etc.). The function should then return this sum.

# For example:

# ```python
# numbers = [1, 5, 2, 8, 3, 9, 4]
# result = sum_of_even_indices(numbers)
# print(result)  # Expected output: 1 + 2 + 3 + 4 = 10
# ```
def sum_of_even_indices(numbers):
    total_sum = 0
    # Iterate through the list with a step of 2 to access only even indices
    for index in range(0,len(numbers),2):
        total_sum += numbers[index]
    return total_sum

numbers = [1, 5, 2, 8, 3, 9, 4]
result = sum_of_even_indices(numbers)    
print(f'sum of {numbers} at even indices is: {result}')