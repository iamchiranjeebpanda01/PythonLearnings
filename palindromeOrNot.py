num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp>0:
    lastDigit = temp%10
    reverse = (reverse*10)+lastDigit
    temp//=10

if num == reverse:
    print(str(num)+ " is a palindrome number")
else:
    print(str(num) + " is not a palidrome number")