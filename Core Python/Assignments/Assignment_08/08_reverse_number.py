# 8. Write a program find reverse of a number

#type 1 : without passig parameter
        #   without return value

def reverse_number():
    num = int(input("Enter a number: "))
    rev = 0
    while num > 0:
        digit = num % 10        # get last digit
        rev = rev * 10 + digit  # build reverse number
        num = num // 10         # remove last digit

    print("Reverse of number =",rev)

reverse_number()

#type 2 : with passig parameter
        #   without return value

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10        # get last digit
        rev = rev * 10 + digit  # build reverse number
        num = num // 10
    print("Reverse of number =",rev)

num = int(input("Enter the number: "))
reverse_number(num)

#type 3 : without  passig parameter
        #   with return value

def reverse_number():
    num = int(input("Enter the number: "))
    rev = 0
    while num > 0:
        digit = num % 10        # get last digit
        rev = rev * 10 + digit  # build reverse number
        num = num // 10
    return rev


res = reverse_number()
print("Reverse of number =",res)

#type 4 : with  passig parameter
        #   with return value

def reverse_number(num):
    num = int(input("Enter the number: "))
    rev = 0
    while num > 0:
        digit = num % 10        # get last digit
        rev = rev * 10 + digit  # build reverse number
        num = num // 10
    return rev


res = reverse_number(num)
print("Reverse of number =",res)
