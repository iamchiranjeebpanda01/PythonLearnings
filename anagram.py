s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1) != len(s2):
    print("Not anagram!")
else:
    for x in s1:
        if x not in s2:
            print("Not anagram!")
            break;
    else:
        print("Anagram!")
    