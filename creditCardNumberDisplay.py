number = int(input("Enter a 16 digit credit card number: "))

while len(str(number)) != 16:
    number = int(input("Please re-enter a 16 digit credit card number: "))

lastFourDigit = str(number)[12:16]
stars = '*' * 4

print(stars + ' ' + stars + ' ' + stars + ' ' + lastFourDigit)