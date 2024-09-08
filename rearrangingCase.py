s1 = input("Enter the string: ")
lower = ''
upper = ''

for x in s1:
    if x.islower():
        lower += x
    else:
        upper += x

    
print(lower+upper)