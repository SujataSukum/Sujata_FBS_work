# 5. Write a program to find factorial using recursion.


def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


num = int(input("Enter the number: "))


res = factorial(num)

print(f"factorial is: ",res)
