from numpy import *
# Write a code to add 2 arrays using for loop
arr1 = array([1,2,3])
arr2 = array([2,2,3])
sum = zeros(3, dtype=int)

result = 0
for i in range(len(arr1)):
    result = arr1[i] + arr2[i]
    sum[i] = result

print(f'Addition of {arr1} & {arr2} is: ',sum)    