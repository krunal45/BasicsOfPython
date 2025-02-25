# contacts = {'krunal':'123-456','james':'456-789'}
# print(contacts['krunal'])
# print(contacts['james'])

# krunal = contacts['krunal']
# print('dial {} to contact Krunal'.format(krunal))
# james = contacts['james']
# print('dial {} to contact James'.format(james))
# contacts['bobby'] = '132-211'
# print(contacts['bobby'])

# del contacts['bobby']
# print(contacts)

# student = {'Name':'Adam','Roll-no':'001'}
# print(student)
# print('{} is name of student & {} is roll-no'.format(student['Name'],student['Roll-no']))

# Tel_Dir = {'Name':'Bob','contacts':['123-456','234-987']}
# contactName = Tel_Dir['Name']
# contacts = Tel_Dir['contacts']
# print('{} is contactName & contact of same is {}'.format(contactName,contacts))

students = {'Name':'Adam','Roll-no':'001'}

# for String in students['Name']:
#     print(String)

# if 'Name' in students:
#     print('Name: '+format(students['Name']))
# else:
#     print('key not present in list!')

# print('Adam' in students.values())

for student in students:
    print('{0} of student is {1}'.format(student,students[student]))