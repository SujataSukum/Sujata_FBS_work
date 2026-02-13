# 7. Find the sum of three-digit number.

number = int(input("enter the three digit number: "))


rm1 = number % 10
number = number // 10

rm2 = number % 10
number = number // 10

rm3 = number % 10

sum = rm1 + rm2 + rm3
print("Sum of three digits number is:", sum)


