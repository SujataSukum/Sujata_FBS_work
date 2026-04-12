
for i in range(1,23):
    for j in range(1,24-i):
        if(i==1 or i+j == 23):
            print("*",end=" ")

        else: print(" ",end=" ")

    for j in range(2,23):
        if(i==22):
            print("*",end=" ")

    print()
