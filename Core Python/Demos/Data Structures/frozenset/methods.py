fs1 = frozenset({10,20,30,40})
fs2 = frozenset({40,50,60,70})

# copy()
# res = fs1.copy()
# print(res)

#difference()   ---Elements in first but not in second
# res = fs1.difference(fs2)
# print(res)

# #intersection      --- Common elements
# res = fs1.intersection(fs2)
# print(res)

# isdisjoint()  ---- return true , if all elements are different in both sets
# res = fs1.isdisjoint(fs2)
# print(res)


#issubset() ---Checks if all elements are inside another set
# res = fs1.issubset(fs2)
# print(res)


# #issuperset()   ----Checks if it contains another set
# print(fs1.issuperset(fs2))

#symmetric_difference ----- elements not common in both sets
# print(fs1.symmetric_difference(fs2))


# union   ---Combines two sets
print(fs1.union(fs2))
