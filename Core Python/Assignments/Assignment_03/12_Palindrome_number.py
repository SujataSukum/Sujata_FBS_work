# 12. Write a program to check if given 3 digit number is a palindrome or not.

number = int(input("Enter the three digit Number: "))
temp = number

rm1 = number % 10
number = number // 10

rm2 = number % 10
number = number // 10

rm3 = number % 10


rev_number = (100 * rm3) + (10 * rm2) + (rm1)


if(temp == rev_number):
    print("Number is Palindrome")


else:
    print("Number is not Palindrome")

