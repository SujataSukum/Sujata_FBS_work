#WAP to check palindrome number using recursion

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    else:
        return reverse_num(num // 10, rev * 10 + num % 10)


def palindrome(num):
    return num == reverse_num(num)


num = int(input("Enter number: "))

if palindrome(num):
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")
