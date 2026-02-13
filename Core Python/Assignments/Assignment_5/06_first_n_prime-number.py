# 6. Write a program to print first n prime numbers.

n = int(input("Enter the number: "))

for n in range(1,n+1):
    count = 0

    for i in range(1,n+1):
        n % i == 0
        count += 1

    if count == 2:
        print(n)

