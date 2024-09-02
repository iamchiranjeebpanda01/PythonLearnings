num = int(input("Enter a number: "))
reverse = 0

while num>0:
    lastDigit = num%10
    reverse = (reverse*10)+lastDigit
    num//=10

print("Reverse of the number is: " + str(reverse))