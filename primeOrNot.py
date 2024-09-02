import math

num = int(input("Enter a number: "))
isPrime = True
sqrt_num = math.ceil(math.sqrt(num))

for i in range(2, sqrt_num+1):
    if num == 2:
        isPrime = True
        break

    if num%i == 0:
        isPrime = False

if isPrime:
    print(str(num) + " is a prime number.")
else:
    print(str(num) + " is not a prime number.")