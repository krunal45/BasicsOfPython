# age = int(input('Enter Age:'));

# if(age>18):
#     print('You are Eligible to vote');
# print('Have a nice day');

# if(age>18):
#     print('You are Eligible to vote');
# else:
#     print('You are Un-Eligible to vote');

# if(age==18):
#     print('You are Eligible to vote');
# elif(age>18):
#     print('You are Eligible to vote');
# else:
#     print('You are Un-Eligible to vote');
# print('Have a nice day');
alphabet1 = input('Enter alphabet 1 :');
alphabet2 = input('Enter alphabet 2 :');
print(type(alphabet1));

if len(alphabet1)!=1 or len(alphabet2) !=1:
    print('Please enter a character of length == 1')
else:
    if(alphabet1>alphabet2):
        print(alphabet1+' is greater than '+alphabet2);
    else:
        print(alphabet2+' is greater than '+alphabet1);