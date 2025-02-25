age = int(input('Enter Age:'))
if(age < 18):
    print('You are uneligible to vote.')
elif(age == 18):
    print('You are eligible to vote.')
else:
    print('Your age is greater than 18')      