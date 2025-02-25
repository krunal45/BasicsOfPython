# Example1
# contacts = {'adam':'123','bob':'234'}
# for contact in contacts:
#     print('Dial {0} to contact {1}'.format(contacts[contact],contact));

# for person,contactNo in contacts.items():
#     print('Dial {0} to contact {1}'.format(contactNo,person))

# Example2
# students = {'alpha':1,'beta':2}
# for student in students:
#     print('Roll no of {1} is {0}'.format(students[student],student))

# for student,rollNo in students.items():
#     print('Roll No of {0} is {1}'.format(student,rollNo))

#Nested Dictionaries:
employees = {
    'John':{
        'Employee ID':'001',
        'Position':'Software Engineer',
        'Department':'IT'
    },
    'Jane':{
        'EmployeeID':'002',
        'Position':'Marketing Manager',
        'Department':'Marketing'
    }
}

# for employee in employees:
#     print(employee)

# for employee in employees:
#     print('Employee Details are :{}{}'.format(employee,employees[employee]))

# for employee,details in employees.items():
#     print('Details of {} is {}'.format(employee,details))

# for employee,details in employees.items():
#     print('Emp ID of {} is {}'.format(employee,employees[employee]['Employee ID']))
#     print('Position of {} is {}'.format(employee,employees[employee]['Position']))
#     print('Department of {} is {}'.format(employee,employees[employee]['Department']))
