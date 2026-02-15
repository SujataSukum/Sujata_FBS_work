# 6. WAP to check if a given number is prime number or not.

num = int(input("Enter a number: "))

i = 1
count = 0

while i <= num:
    if num % i == 0:
        count = count + 1
    i = i + 1

if count == 2:
    print(f"{num} is Prime Number")
else:
    print(f"{num} is Not a Prime Number")
