password1 = input("Enter password1: ")
password2 = input("Enter password2: ")

if password1 == password2:
    print("Passwords matched!")
elif password1.lower() == password2.lower():
    print("Please check for cases in both passwords.")
else:
    print("Password didn't match!")