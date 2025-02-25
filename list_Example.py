nums = [1,2,3]
print(nums)
nums.append(4)
for num in nums:
    print(num)

nums.sort(reverse=True)
print(nums)

minimumNumber = min(nums)
print('minimumNumber > '+str(minimumNumber))

maximumNumber = max(nums)
print('maximumNumber > '+str(maximumNumber))

nums.extend([5,6,7,8])
print(nums)

nums.insert(1,9)
print(nums)

# num = nums.pop(0)
# print(num)

# num = nums.pop()
# print(num)

newNums = nums.copy()
for index in range(len(newNums)-1,-1,-1):
    print(newNums[index])