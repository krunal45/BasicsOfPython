from numpy import *
# Different ways of array creation
# Method 1
arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

# Method 2
arr1 = linspace(1,16,16)
print(arr1)

# Method 3
arr2 = arange(1,10,2)
print(arr2)

# Method 4
arr3 = logspace(1,10,5)
print(arr3)

# Method 5
arr4 = zeros(5)
print(arr4)

# Method 6
arr5 = ones(5)
print(arr5)