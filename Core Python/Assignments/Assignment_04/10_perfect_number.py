# 10. WAP to check if given number is Perfect Number.

num = int(input("Enter the number: "))

i = 1
sum = 0

while(i<num):
    if(num % i == 0):
        sum += i
    i += 1

if(num == sum):
    print(f'{num} is a Perfect Number')

else:
    print(f'{num} is Not a perfect number ')
