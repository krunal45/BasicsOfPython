from numpy import *

arr1 = array(['a','b','c','d'])
arr2 = arr1.copy()
print(arr2)

num1 = array([1,2,4])
num2 = array([5,6,4])
# Finding minimum number in array
print(f'Minimum Number :',min(num1))
# Finding maximum number in array
print(f'Maximum Number :',max(num1))
# Finding sum in array
print(f'sum of {num1} elements: ',sum(num1))
# Finding multiplication of array
result = 1
for i in range(len(num1)):
    result = result * num1[i]

print(result)
# Adding 2 arrays
result = num1 + num2
print(result)