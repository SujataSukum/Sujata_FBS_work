# a. 1+ 2 + 3 + 4+..... + n

#type 1 : without passig parameter
        #   without return value
def sum_series():
    n = int(input("Enter the value of n: "))
    sum=0
    for i in range(1,n+1):
        sum += i

    print("Sum of the series is: ",sum)

sum_series()

#type 2 : with passing parameter
#         without return value

def sum_series(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(f'Sum of the series is {sum}')

n = int(input("Enter the value of n: "))

sum_series(n)


#type 3 : without passing parameter
#         with return value

def sum_series():
    n = int(input("Enter the value of n: "))

    sum = 0
    for i in range(1,n+1):
        sum  += i

    return sum

res = sum_series()
print("Sum of series is: ",res)

#type 4 : with passing parameter
#         with return value

def sum_series(n):

    sum  = 0
    for i in range(1,n+1):
        sum += i

    return sum

n = int(input("Enter the value of n: "))

res = sum_series(n)
print("Sum of series is: ",res)
