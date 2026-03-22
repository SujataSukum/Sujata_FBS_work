# 5. Sum of all prime numbers between 1 to n

#type 1 : without passig parameter
        #   without return value

def sum_prime():
    n = int(input("Enter value of n: "))
    total = 0

    for i in range(1, n + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1

        if count == 2:   # prime number
            total = total + i

    print("Sum of prime numbers =", total)


# function call
sum_prime()

#type 2 : with passig parameter
        #   without return value

def sum_prime(n):
    total = 0

    for i in range(1, n + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1

        if count == 2:
            total = total + i

    print("Sum of prime numbers =", total)



n = int(input("Enter value of n: "))
sum_prime(n)

#type 3 : without  passig parameter
        #   with return value

def sum_prime():
    n = int(input("Enter value of n: "))
    total = 0

    for i in range(1, n + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1

        if count == 2:
            total = total + i

    return total


# function call
result = sum_prime()
print("Sum of prime numbers =", result)


#type 3 : with  passig parameter
        #   with return value

def sum_prime(n):
    total = 0

    for i in range(1, n + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1

        if count == 2:
            total = total + i

    return total


# input
n = int(input("Enter value of n: "))
print("Sum of prime numbers =", sum_prime(n))
