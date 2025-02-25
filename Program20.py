# with open('/Users/krunalb/Desktop/test1') as file:
#     print(file.mode)

# with open('/Users/krunalb/Desktop/test1','w') as file:
#     print(file.mode)
#     file.write('This is line 4.')

# with open('/Users/krunalb/Desktop/test1') as file:
#     print(file.read())   

# with open('/Users/krunalb/Desktop/test1','a') as file:
#     file.write('\nThis is line 5.')

# with open('/Users/krunalb/Desktop/test1') as file:
#     print(file.read()) 

with open('/Users/krunalb/Desktop/test2','x') as file:
    file.write('This is line 1.')
    file.write('\nThis is line 2.')

with open('/Users/krunalb/Desktop/test2') as file:
    print(file.read())