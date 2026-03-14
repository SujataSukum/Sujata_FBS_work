def add(a,*numbers):
    sum=0
    for num in numbers:
        sum += num

    return sum

res = add('a',10,20,30,40)
print(res)
