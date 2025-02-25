# fruits = ['apple','banana','chickoo','Dry Fruits']
# newList = []

# for x in fruits:
#     if 'D' in x:
#         newList.append(x)

# print(newList)

fruits = ['apple','banana','chickoo','Dry Fruits']
newList = [x for x in fruits if 'b' in x]
print(newList)

newList = [x for x in fruits if 'chickoo'!=x]
print(newList)

num = [x for x in range(10) if x<4]
print(num)

newList=[x if x!='banana' else 'orange' for x in fruits]
print(newList)       