# 11. WAP to check if given number Strong Number.

# A Strong Number is  The sum of factorial of its digit is equal to the number itself.

'''
Input  : n = 145
Output : Yes
Sum of digit factorials = 1! + 4! + 5!
                        = 1 + 24 + 120
                        = 145
Input :  n = 534
Output : No
'''

num = int(input('Enter the number: '))

original_num = num

sum_fact = 0


while num > 0:
    digit = num % 10           # print last digit

    fact = 1            # every iteration store factoriale of each numer

    for i in range(1,digit+1):                  # loop for calculate the factorial
        fact = fact * i

    sum_fact = sum_fact + fact           # store factorial of all number one by one
    num = num // 10              # remove the last digit

if sum_fact == original_num:
    print(f'{original_num} is a Strong number.')
else:
    print(f'{original_num} is not a Strong number')
