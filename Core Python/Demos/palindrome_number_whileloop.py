# WAP to check whether number is palindrome or not

num = int(input("Enter the number: "))

temp = num
rev_num = 0

while(temp > 0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num  * 10 + d

if(num == rev_num):
    print(f'{num}is Palindrome number')

else:
    print(f'{num}is not palindrome number')

