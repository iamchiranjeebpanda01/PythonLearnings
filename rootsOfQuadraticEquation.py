import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

discrimant = b**2 - 4*a*c

if discrimant<0: 
    print("The roots of the provided equation are complex numbers")
else:
    root1 = (-b + math.sqrt(discrimant))/(2*a)
    root2 = (-b - math.sqrt(discrimant))/(2*a)

    print(discrimant)
    print("The roots of the provided equation are: " + str(root1) + " and " + str(root2))