# **Question:**

# Write a Python program that loops through a list of fruits.  
# If the fruit is `"banana"`, do nothing (use the `pass` statement).  
# For all other fruits, print their name.

# Here’s the list to use:
# ```python
# fruits = ["apple", "banana", "cherry", "mango"]
# ```
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    if fruit == 'banana':
        pass
    else:
        print(fruit)