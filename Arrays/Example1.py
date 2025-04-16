from array import *

alphabets = array('u',['A','B','C','D'])

# Way 1
for alphabet in alphabets:
    print(alphabet,end=" ")

print()
# Way 2
for index in range(len(alphabets)):
    print(alphabets[index],end=" ")

# Reverse array
alphabets.reverse()
print(alphabets)

# Duplicating Array
copyOfAlphabets = array(alphabets.typecode,(a for a in alphabets))
for alphabet in copyOfAlphabets:
    print(alphabet,end=" ")