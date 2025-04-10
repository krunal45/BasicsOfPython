# Write code to print all values from 1 to 100. Skip numbers that are divisible by 3 or 5
i = 1
while i <= 100:
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    i += 1    