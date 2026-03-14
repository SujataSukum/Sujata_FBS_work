# Type 4 function
#  with passing parameter (with input)
#  with returning value (with output)


def addition(num1,num2):
    sum = num1 +num2

    return sum

num1= int(input("Enter the number 1: "))
num2 = int(input("Enter number 2: "))

res = addition(num1,num2)

print(f'Addition of {num1} and {num2} is {res}')
