myString = input("Enter a string: ")
reverseString = myString[::-1]

if myString.lower() == reverseString.lower():
    print(myString + " is a pallindrome")
else:
    print(myString + " is not a pallindrome")