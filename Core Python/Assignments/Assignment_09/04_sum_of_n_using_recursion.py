# 4. Write a program to find sum of n numbers using recursion.


def sum_number(n):
    if n == 1:
        return 1
    else:
        return n + sum_number(n-1)

n = int(input("Enter value of n: "))

res = sum_number(n)

print("Sum of n numbers is: ",res)
