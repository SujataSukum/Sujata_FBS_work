#9. WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

divisor = int(input("Enter the Divisor number: "))

i = start

while(i<=end):
    if i % divisor == 0:
        print(i)
    i += 1
