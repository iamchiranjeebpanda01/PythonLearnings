import random

original_Number = random.randint(1, 10)

print("The number is between 1-10. Let's start begin!")
guess_Number = int(input("Enter the guess number: "))

while original_Number != guess_Number:
    if original_Number > guess_Number:
        print("Make a greater guess ;)")
        guess_Number = int(input("Enter the guess number: "))
    else: 
        print("make a smaller guess ;)")
        guess_Number = int(input("Enter the guess number: "))

if original_Number == guess_Number:
    print("Correct Guess! You won :)")