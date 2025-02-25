def reverseData(input):
    dataArr = [str(character) for character in input]
    output = []
    for index in range(len(dataArr)-1,-1,-1):
        output.append(dataArr[index])
    return ('').join(output)   

data = input('Please Enter a Number or String to reverse: ') 
print('Reversed data > '+reverseData(data))