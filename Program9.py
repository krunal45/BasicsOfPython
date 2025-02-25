fruits = ['apple','banana','chickoo']
apple_index = fruits.index('apple')
print('index of apple : '+str(apple_index))

try:
    dragon_index = fruits.index('dragon')
except:
    dragon_index = 'dragon is not in list'
print(dragon_index)