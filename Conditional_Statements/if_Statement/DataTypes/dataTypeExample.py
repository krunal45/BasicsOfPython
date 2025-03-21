# Numeric 
num1 = 1
print(type(num1))
num2 = 1.2
print(type(num2))
num1 = int(num2)
print('num1: ',num1)
num3 = 4
num4 = 5
c = num3 + num4*1j
print(type(c))
d = complex(num3,num4)
print('complexNumber: ',d)

# Boolean
flag1 = True
print(type(flag1))
flag2 = bool(num1)
print('1 in boolean is: ',flag2)
flag2 = bool(0)
print('0 in boolean is: ',flag2)

# String
name1 = 'Ajay'
print(type(name1))
alphabet = 'A'
print(type(alphabet))

# Sequence
fruits = ['Apple','Banana','Chickoo','Dragon Fruit']
print(type(fruits))

weekEnds = {'Sat','Sun'}
print(type(weekEnds))

weekDays = ('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
print(type(weekDays))

weekEndPlan = {weekDays[5]:'IPL',weekDays[6]:'Movie'}
print(weekEndPlan)
print(type(weekEndPlan))
keys = weekEndPlan.keys()
values = weekEndPlan.values()
print('Keys: ',keys)
print('Values: ',values)