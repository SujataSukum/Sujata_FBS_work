# 4. WAP to print Armstrong number within a given range

# Enter range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong numbers in the given range are:")

for num in range(start, end + 1):

    temp = num
    digits = len(str(num))  # Count number of digits
    sum = 0

    while temp > 0:
        digit = temp % 10        # to print last digit
        sum += digit ** digits
        temp = temp // 10        # remove last digit

    if sum == num:
        print(num)


