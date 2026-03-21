# 9. Write a program to check if entered number is a palindrome or
# not.

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
