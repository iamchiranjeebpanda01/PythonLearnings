s1 = input("Enter the string: ")
punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~ """

s2=''

for x in s1:
    if x not in punctuations:
        s2 += x


print(s2)