myString = input("Enter a string: ")
reverseString = myString[::-1]

if myString.lower() == reverseString.lower():
    print(myString)
else:
    print(myString+reverseString)