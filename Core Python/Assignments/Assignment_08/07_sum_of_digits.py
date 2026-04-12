# 7. Write a program to find sum of digits of a number.

#type 1 : without passig parameter
        #   without return value

def sum_of_digits():
    num = int(input("Enter a number: "))
    total = 0

    while num > 0:
        digit = num % 10      # get last digit
        total = total + digit
        num = num // 10       # remove last digit

    print("Sum of digits =", total)

sum_of_digits()


#type 2 : with passig parameter
        #   without return value

def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    print("Sum of digits =", total)

num = int(input("Enter the number: "))

sum_of_digits(num)

#type 3 : without passig parameter
        #   with return value

def sum_of_digits():
    num = int(input("Enter a number: "))
    total = 0

    while num > 0:
        digit = num % 10      # get last digit
        total = total + digit
        num = num // 10       # remove last digit
    return total


res = sum_of_digits()
print("Sum of digits =", res)


#type 4 : with passig parameter
        #   with return value

def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10      # get last digit
        total = total + digit
        num = num // 10       # remove last digit
    return total

num = int(input("Enter a number: "))

res = sum_of_digits(num)
print("Sum of digits =", res)
