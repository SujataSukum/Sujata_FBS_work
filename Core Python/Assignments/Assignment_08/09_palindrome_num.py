# 9. Write a program to check if entered number is a palindrome or
# not.

#type 1 : without passig parameter
        #   without return value

def palindrome():
    num = int(input("Enter a number: "))
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if temp == rev:
        print(temp, "is a Palindrome")
    else:
        print(temp, "is not a Palindrome")


# function call
palindrome()

#type 2 : with passig parameter
        #   without return value

def palindrome(num):
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if temp == rev:
        print(temp, "is a Palindrome")
    else:
        print(temp, "is not a Palindrome")

num = int(input("Enter a number: "))
# function call
palindrome(num)

#type 3 : without  passing parameter
        #   with return value

def palindrome():
    num = int(input("Enter a number: "))
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if temp == rev:
        return temp, True
    else:
        return temp, False


# function call
num, res = palindrome()

if res:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")


#type 4 : with  passing parameter
        #   with return value
def palindrome(num):
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return temp == rev   # returns True or False


# input
n = int(input("Enter a number: "))

# function call
if palindrome(n):
    print(n, "is a Palindrome")
else:
    print(n, "is not a Palindrome")
