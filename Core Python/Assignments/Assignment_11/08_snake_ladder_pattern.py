num = 1

for row in range(1, 11):   # 10 rows
    temp = []

    for col in range(1, 11):   # 10 columns
        temp.append(num)
        num += 1

    # reverse for even rows
    if row % 2 == 0:
        temp.reverse()

    # print row
    for i in temp:
        print(i, end="\t")
    print()
