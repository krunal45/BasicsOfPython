# In Dictionary data is stored in 'Key' | 'Value' format
# names = {'A':'Apple','B':'Banana','C':'Chickoo','D':'Dragon'}
# print(names)
# # In order to fetch a particular value we need to fetch it using 'Key'
# print(names['A'])

# # We can also fetch a particular value using following method
# print(names.get('A'))

# # We can also choose tp print Error in case if corresponding value is not found against key
# print(names.get('E','Not Found!'))

# We can merge 2 lists into dictionary!
states = ['Gujarat','W. Bengal','Jharkhand']
capitals = ['Gandhinagar','Kolkata','Ranchi']
stateCapitals = dict(zip(states,capitals))
print(stateCapitals)

# Add data to dictionary
stateCapitals['M.Pradesh'] = 'Indore'
print(stateCapitals)

# Deleting data from dictionary
del stateCapitals['M.Pradesh']
print(stateCapitals)

data = {'A':'Apple','B':'Banana','Python':['pycharm','submime'],'Java':{'JavaSE':'Eclipse','JavaEE':'Netbeans'}}
print(data['A'])
print(data['Python'][0])
print(data['Java']['JavaSE'])