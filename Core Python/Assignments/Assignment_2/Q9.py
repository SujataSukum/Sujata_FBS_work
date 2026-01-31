#9. Write a program to swap two numbers without using third variable.

n1 = int(input("Enter the First Number: "))
n2 = int(input("Enter the second number "))


n1 , n2 = n2 , n1


print(f"after swapping the numbers:{n1},{n2}")
