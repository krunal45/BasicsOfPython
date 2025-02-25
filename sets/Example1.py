# sets won't maintain the insertion order
# sets won't allow duplicate values
set1 = {'Maharastra','Gujarat','Delhi','West Bengal',1,2,3}
print(set1)

# Using For - Each Loop
for set in set1:
    print(set)

# sets do not maintain index. Hence we can't use normal for loop
# It will throw below error > 
# TypeError: 'set' object is not subscriptable
# for index in range(len(set1)):
#     print(set1[index])   

# using add() > we can add new element to the set.
set1.add('4')
print(set1)

# using update() > we can append other sets to the existing one. 
# We can't add individual members though if we try to do then it will throw error.
# Like >   set1.update(5)   ~~~~~~~~~~~^^^
# TypeError: 'int' object is not iterable
# set1.update(5)

set2 = {'Apple','Banana','Chickoo'}
set1.update(set2)
print(set1)

nums = {1,2,3,4,5}
print('Before Delete > '+str(nums))
nums.remove(3)
print('After Delete > '+str(nums))