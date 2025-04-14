availableCandies = 5
inputCandies = int(input('Enter number of candies: '))
i = 1
while i<=inputCandies:
    if i > availableCandies:
        print('out of stock!')
        break
    print('candy ',i)
    i+=1
print('Bye')    