# animals = ['cat','dog','sheep']
# few_animals = animals[:1]
# print('{} is mother'.format(few_animals))
# few_animals = animals[:2]
# print(few_animals)
# few_animals = animals[1:2]
# print(few_animals)
# few_animals = animals[-1:]
# print(few_animals)

fruits = ['apple','banana','chickoo','Durian','Elderberry','Fig','Grapes']
few_fruits = fruits[0:2]
print(few_fruits)
few_fruits.insert(0,'cherry')
print(few_fruits)
few_fruits.insert(2,'coconut')
print(few_fruits)
fruit1= fruits[-4]
print(fruit1)
print('fewFruits > Reverse order')
few_fruits.reverse()
print(few_fruits)
indexValue = few_fruits.index('banana')
print(indexValue)
copy_few_fruits = few_fruits.copy()
print('copy > few_fruits - ')
print(copy_few_fruits)
#This will sort list in ascending order
few_fruits.sort()
print(few_fruits)

#This will sort list in descending order
few_fruits.sort(reverse=True)
print(few_fruits)