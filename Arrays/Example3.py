from array import *
# Create an array with 5 values & delete the value at index no. 2 without using in-built function.
arr = array('i',[1,2,3,4,5])

for i in range(len(arr)):
    if i == 2:
        del arr[i]
        break
print(arr)