def say_hi():
    print('hi!')
say_hi()

def printName(name):
    print(name)
printName('Krunal')

def printName1(name='Krunal'):
    print('Hi {}'.format(name))
printName1()

def printName2(fname,lname):
    print('hi {} {}'.format(fname,lname));
printName2('Krunal','Bhatt')