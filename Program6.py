# num1 = int(input('Please Enter Number: - '))
# def is_odd_Even(num):
#     if(num%2==0):
#         return True
#     else:
#         return False
# print(str(num1)+' is Even: '+str(is_odd_Even(num1)))

# def is_odd_Even_Number(num):
#     if num % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
# print(str(num1)+' is '+is_odd_Even_Number(num1))  




def enter_name():
    name = input('Enter Name: - ')
    return name

def enter_age():
    age = input('Enter Age: -')
    return age

def display_Name_and_age(): 
    print('Name: '+enter_name())
    print('Age: '+enter_age())

display_Name_and_age()