# c. 1^1 + 2^2 + 3^3+ ...... n^n

#type 1 : without passing parametre
#         without return value


def sum_of_power():
    n = int(input("Enter value of n: "))
    total = 0
    for i in range(1, n + 1):
        total = total + (i ** i)
    print("Sum of exponential is: ",total)
sum_of_power()

#type 2 : with passing parametre
#         without return value

def sum_of_power(n):
    total = 0
    for i in range(1, n + 1):
        total = total + (i ** i)
    print("Sum of exponential is: ",total)

n = int(input("Enter the value of n: "))
sum_of_power(n)


#type 3 : without passing parametre
#         with return value


def sum_of_power():
    n = int(input("Enter the value of n: "))
    total = 0
    for i in range(1, n + 1):
        total = total + (i ** i)
    return total

res = sum_of_power()
print("Sum of exponential is: ",res)

#type 4: with passing parametre
#         with return value

def sum_of_power(n):

    total = 0
    for i in range(1, n + 1):
        total = total + (i ** i)
    return total

n = int(input("Enter the value of n: "))
res = sum_of_power(n)

print("Sum of exponential is: ",res)
