# li = [10,20,30,40,50]

# sum = 0

# for i in range(0,len(li)):
#     sum += li[i]

# print(sum)


# # WAp to create list according to user

# li = []

# n = int(input("Enter the number of elements: "))

# for i in range(n):
#     element = input("Enter Element: ")
#     li.append(element)


# print(li)


#WAP to find maximum number from list

li = [30,70,25,84,32,90,20,10]


max = li[0]


for i in range(1,len(li)):
    if li[i] > max :
        max = li[i]


print(max)
