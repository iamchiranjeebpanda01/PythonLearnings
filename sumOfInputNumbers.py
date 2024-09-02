total_nums = int(input("Enter the total number of inputs: "))
sum = 0

while total_nums>0:
    num = int(input("Enter a new number: "))
    sum += num
    total_nums -= 1

print("Sum of all the numbers is: " + str(sum))