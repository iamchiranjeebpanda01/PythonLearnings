terms = int(input("Enter the number of terms for the fibonnaci series: "))
t1 = 0
t2 = 1

for i in range(0, terms):
    print(t1)

    temp = t2
    t2 += t1
    t1 = temp