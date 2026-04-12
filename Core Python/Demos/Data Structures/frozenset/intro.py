# structure = {()}

s1 = frozenset({10,20,30.40})
print(type(s1))

# type of data --- heterogeneous
s1 = ({10,3.17,'a','b'})
print(s1)

# sequence = unordered

# chanagble -  immutable

# # not editable
fs = frozenset({10,20,30})
fs.add(40)
print(fs)
