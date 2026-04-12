# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

#type 1 : without passig parameter
        #   without return value


def armstrong():
    num = int(input("Enter a number: "))
    temp = num
    total = 0

    while num > 0:
        digit = num % 10
        total = total + (digit ** 3)
        num = num // 10

    if total == temp:
        print(temp, "is an Armstrong number")
    else:
        print(temp, "is not an Armstrong number")


# function call
armstrong()

#type 2 : with passig parameter
        #   without return value

def armstrong(num):

    temp = num
    total = 0

    while num > 0:
        digit = num % 10
        total = total + (digit ** 3)
        num = num // 10

    if total == temp:
        print(temp, "is an Armstrong number")
    else:
        print(temp, "is not an Armstrong number")

num = int(input("Enter a number: "))
# function call
armstrong(num)

#type 3 : without passig parameter
        #   with return value


def armstrong():
    num = int(input("Enter a number: "))
    temp = num
    total = 0

    while num > 0:
        digit = num % 10
        total = total + (digit ** 3)
        num = num // 10

    if total == temp:
        return temp, True
    else:
        return temp, False


# function call
num, res = armstrong()

if res:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


#type 4 : with passig parameter
        #   with return value

def armstrong(num):
    temp = num
    total = 0

    while num > 0:
        digit = num % 10
        total = total + (digit ** 3)
        num = num // 10

    if total == temp:
        return True
    else:
        return False


# input
n = int(input("Enter a number: "))

# function call
if armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
