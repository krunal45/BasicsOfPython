# **Question**: Write a Python program that asks the user to input a temperature (as an integer) 
# and then prints:
# - "Hot" if the temperature is 30 or higher,
# - "Warm" if the temperature is between 15 and 29 (inclusive),
# - "Cold" if the temperature is below 15.
temperature = int(input('Please enter Temperature: '))
if temperature<15:
    print('Cold')
elif temperature >=15 and temperature <=29:
    print('Warm')    
else:
    print('Hot')