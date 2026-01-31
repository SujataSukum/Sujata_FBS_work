# 10. Write a program to reverse three-digit number.

number = int(input("enter the three digit number: "))


rm1 = number % 10
number = number // 10

rm2 = number % 10
number = number // 10

rm3 = number % 10


rev_number = (100 * rm1) + (10 * rm2) + (rm3)

print(f"reverse of the three digit number is: {rev_number}")
