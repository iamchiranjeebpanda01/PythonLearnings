total_nums = int(input("Enter the total number of numbers: "))
maxNum = int(input("Enter a new number: "))

while total_nums-1 > 0:
    num = int(input("Enter a new number: "))
    
    if maxNum < num:
        maxNum = num

    total_nums -= 1
    
print("The maximum number entered is: " + str(maxNum))