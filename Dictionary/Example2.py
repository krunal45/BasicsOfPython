# 'Alice': {'age': 22, 'major': 'Computer Science', 'GPA': 3.8}
Alice = {'age': 22, 'major': 'Computer Science', 'GPA': 3.8}
age = Alice['age']
major = Alice['major']
GPA = Alice['GPA']
print('Age : '+str(age))
print('Major: '+major)
print('GPA:'+str(GPA))

students = {
    'Alice': {'age': 22, 'GPA': 3.8},
    'Bob': {'age': 21, 'major': 'Mathematics', 'GPA': 3.6}
}
# Fetching data of 'Alice'
print(students['Alice']['age'])
print(students['Alice']['major'])

# Fetching data of 'Bob'
print(students['Bob']['major'])

students['Alice'].setdefault('major','Science')
print(students['Alice']['major'])