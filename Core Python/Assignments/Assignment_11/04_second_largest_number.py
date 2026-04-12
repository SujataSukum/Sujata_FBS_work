# take list from user
li = list(map(int, input("Enter numbers: ").split()))

n = len(li)

# Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        if li[j] > li[j + 1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

# print sorted list
print("Sorted list:", li)

# find second largest
if n < 2:
    print("No second largest number")
else:
    print("Second largest number is:", li[n - 2])
