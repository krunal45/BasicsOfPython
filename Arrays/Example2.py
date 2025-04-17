from array import *

# Taking array input from user
lengthOfArray = int(input('Enter length of Array :'))
nums = array('i',[]) #Creating blank array

for i in range(lengthOfArray):
    val = int(input('Please enter next value :'))
    nums.append(val)

print(nums)

# searching index value of number
# Manual path
count = 0
val = int(input('Enter number to search :'))
for num in nums:
    if val == num:
        print(count)
        break
    count+=1 

# Using inbuilt python function
print(f'index :{nums.index(val)}')