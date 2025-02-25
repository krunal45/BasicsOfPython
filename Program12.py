fruits = ['dragon','cherry','kiwi']
print('Fruits without sorting > {}'.format(fruits))
sorted_fruits = sorted(fruits)
print('Fruits with sorting > {}'.format(sorted_fruits))

fruits.sort(reverse=True)
print('Fruits with sorting > {}'.format(fruits))