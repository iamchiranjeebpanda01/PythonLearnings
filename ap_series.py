start = int(input("Enter the starting number for the series: "))
common_diff = int(input("Enter the common difference for the series: "))
total_terms = int(input("Enter the total terms required for the AP series: "))

for i in range(start, start+total_terms*common_diff, common_diff):
    print(i)

