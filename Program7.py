animal = ['dog','bear','dear'];
print(animal)
print(animal[0])
print(animal[2])
print(animal[-1])
print(animal[-2])
print(animal[-3])
animal[0] = 'cat'
print(animal)
animal[-1] = 'horse'
print(animal)
animal.append('cow')
print(animal)
more_animals = ['buffalo','goat','cat']
animal.extend(more_animals)
print(animal)
animal.remove('goat')
animal.remove('cat')
print(animal)