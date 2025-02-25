alphabets = {'A':'Apple','B':'Banana','C':'Chickoo','D':'DragonFruit'}
print(alphabets['A'])

for key in alphabets:
    print(f'Key: {key}, Value: {alphabets[key]}')

print(alphabets.get('A'))
print(alphabets.get('E','Not Found!'))

keys = ['Gujarat','UP','W.Bengal']
values = ['Gandhinagar','Lucknow','Kolkata']
states = dict(zip(keys,values))
print(states)

# Adding new state into dictionary
states['Maharashtra'] = 'Mumbai'
print(states)

# Deleting state from dictionary
del states['Maharashtra']
print(states)

programingLangs = {'JS' : 'Atom','CS':'VisualStudio','Python':['Pycharm','SubLime'],'Java':{'JEE':'Netbeans','JSE':'Eclipse'}}
print(programingLangs['JS'])
print(programingLangs['Python'][0])
print(programingLangs['Java']['JSE'])
print(programingLangs.get('Java')['JEE'])