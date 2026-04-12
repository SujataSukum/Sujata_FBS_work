# 1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

# recursive function to find factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#recursive function to find sum of series

def sum_series(n):
    if n == 1:
        return 1
    else:
        return factorial(n) + sum_series(n-1)

n = int(input("Enter the value of n: "))

res = sum_series(n)

print("Sum of series: ",res)
