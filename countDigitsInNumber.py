num = int(input("Enter the number: "))
digitCount = 0

while num>0:
    num//=10
    digitCount+=1

print("The number of digits is: " + str(digitCount))