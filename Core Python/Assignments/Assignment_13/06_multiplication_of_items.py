# 6. Python Program to Multiply All the Items in a Dictionary

di ={"a":10,"b":20,"c":30,"d":40}

total = 1

for key in di:
    total *= di[key]

print("Product of all items: ",total)
