#syntax
# map(function,iterables)

data = [1,2,3,4,5,6,7,8,9,10]

#method 1

sq = lambda x : x ** 2

res = list(map(sq,data))
print(res)

# method 2

res = list(map(lambda x: x ** 2,data))
print(res)


# after iterating elemnts from iterables

for i in res:
    print(i)
