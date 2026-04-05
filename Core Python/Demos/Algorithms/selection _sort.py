def selectionSort():
    size = len(li)

    for i in range(0,size-1):
        ind = i

        for j in range(i+1, size):
            if li[ind] > li[j]:
                ind = j

        li[i] , li[ind] = li[ind] , li[i]


li = [60,30,10,40,20]

print('Before swpping li: ',li)

selectionSort()

print('After Swapping li: ',li)
