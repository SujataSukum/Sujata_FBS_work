# 2. Write a program to check if given number is Armstrong or not using recursive
# function.

#recursive function to calculate sum of powers
def armstrong_sum(n,power):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return (digit ** power) + armstrong_sum(n // 10,power)

num = int(input("Enter a number: "))

#count number of digits
power = len(str(num))

res = armstrong_sum(num,power)

#check armstrong

if res == num:
    print("Armstrong Number")

else:
    print("Not Armstrong Number")
