decimal = int(input("Enter a number: "))
reverseBinary = ''

while decimal>0:
    reverseBinary = str(decimal%2) + reverseBinary
    decimal//= 2

print("The number in binary is: " + reverseBinary)