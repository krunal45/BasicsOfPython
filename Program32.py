l1 = ['a','b','c']
l2 = [1,2]
l3 = l1 + l2
print(l3)

l1 = ['d','e','f']
l2 = [1,2,3]

for x in l2:
    l1.append(x)
print(l1)

l1 = [1,2,3]
l2 = [4,5]
l1.extend(l2)
print(l1)