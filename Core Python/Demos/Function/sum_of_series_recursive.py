def sumOfSeries(n):
    if(n>0):
        return n + sumOfSeries(n-1)

    elif(n==0):
        return 0

    else:
        return None

n=5
res=sumOfSeries(n)
print(res)
