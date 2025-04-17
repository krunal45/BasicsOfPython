from array import *
# write a code to reverse an array without using in-built function.

arr = array('i',[1,2,3,4])
print(arr)

# Reverse Array
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")