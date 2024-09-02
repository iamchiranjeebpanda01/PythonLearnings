total_nums = int(input("Enter the number of inputs: "))
positive_sum = 0
negative_sum = 0

while total_nums > 0:
    num = int(input("Enter a new number: "))

    if num>=0:
        positive_sum += num
    else:
        negative_sum += num

    total_nums -= 1

print("Sum of positive numbers is: " + str(positive_sum))
print("Sum of negative numbers is: " + str(negative_sum))