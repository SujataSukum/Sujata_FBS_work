# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

# take input
s = input("Enter a string: ")

# check length
if len(s) < 2:
    print("New string:", s)
else:
    first = s[0]
    last = s[len(s) - 1]

    middle = ""

    # build middle part
    for i in range(1, len(s) - 1):
        middle = middle + s[i]


    new_string = last + middle + first

    print("New string:", new_string)
