# tuple > 
# 1. Same as list but it is immutable i.e we can't alter it's value.
# 2. Maintains insertion order.
# step 1 > how to define ? 
stateCapitals = ('Delhi','Gandhinagar','Mumbai','Lucknow','Delhi')
# print(stateCapitals)

# # step 2 > using for - Each loop
# # for capital in stateCapitals:
# #     print(capital)

# # step 3 > using normal for loop > ascending
# print('--ascending--')
# for index in range(len(stateCapitals)):
#     print(stateCapitals[index])

# # step 3.1 > using normal for loop > descending
# print('--descending--')
# for index in range(len(stateCapitals)-1,-1,-1):
#     print(stateCapitals[index])

# count > Will state number of occurences of value.
print(stateCapitals.count('Delhi'))

# index > Will return index of the first occurence of value.
print(stateCapitals.index('Delhi'))

# __contains__ > verifies if value is Present ? 
print('is Delhi Present in tuple?: '+str(stateCapitals.__contains__('Delhi')))
print('is Ranchi Present in tuple?: '+str(stateCapitals.__contains__('Ranchi')))

# __add__ > can only concatenate tuple (not "str") to tuple
nationalCapital = ('Tunis','Ankara','Ashgabat')
print(stateCapitals.__add__(nationalCapital))