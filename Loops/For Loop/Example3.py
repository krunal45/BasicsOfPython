# **Question:**

# Write a Python function called `print_multiplication_table` that takes an integer `n` as input.
# The function should use nested `for` loops to print the multiplication table up to `n` x `n`.
# Each row of the table should display the multiplication of the current row number with numbers
# from 1 to `n`.

# For example, if `n` is 3, the output should be:

# ```
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ```
def print_multiplication_table(number):
    """
    Prints the multiplication table up to `number` x `number`.

    Args:
        number (int): The size of the multiplication table.
    """
    result = ""
    for row in range(1, number+1):
        for col in range(1, number+1):
            result += f'{row} x {col} = {row*col}\n'

while True:
    try:
        number = int(input('Please Enter Number: '))
        print_multiplication_table(number)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")