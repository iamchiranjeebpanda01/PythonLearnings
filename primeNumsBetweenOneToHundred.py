import math

print(2)

for i in range(3, 101):
    isPrime = True
    sqrt_i = math.ceil(math.sqrt(i))

    for j in range(2, sqrt_i+1):
        if i%j == 0:
            isPrime = False

    
    if isPrime:
        print(i)