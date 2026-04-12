# b. 1!+ 2! + 3! + 4!+..... + n!

#type 1 : without passing parametre
#         without return value

def sum_fact():
    n = int(input("Enter the value of n: "))
    fact = 1
    total = 0

    for i in range(1,n+1):
        fact *= i
        total = total + fact

    print("Sum of factorial is: ",total)

sum_fact()

#type 2 : with passing parametre
#         without return value

def sum_fact(n):
    fact = 1
    total = 0

    for i in range(1,n+1):
        fact *= i
        total = total + fact
    print("Sum of factorial is: ",total)

n = int(input("Enter the value of n: "))
sum_fact(n)

#type 3 : without passing parametre
#         with return value


def sum_fact():
    n = int(input("Enter the value of n: "))
    fact = 1
    total = 0

    for i in range(1,n+1):
        fact *= i
        total = total + fact

    return total

res = sum_fact()
print("Sum of factorial is: ",res)


#type 4 : with passing parametre
#         with return value

def sum_fact(n):
    fact = 1
    total = 0

    for i in range(1,n+1):
        fact  *= i
        total = total + fact

    return total

n = int(int(input("Enter the value of n: ")))

res = sum_fact(n)
print("Sum of factorial is: ",res)
