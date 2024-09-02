num = int(input("Enter the number: "))
sum = 0

while num>0:
    sum += num%10
    num//=10

print("Sum of digits of the number is: " + str(sum))