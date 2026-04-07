# capitalize()

str = 'FirstBit Solution'
res = str.capitalize()
print(res)

#count()

res = str.count('Bit')
print(res)

#endswith()
res = str.endswith('ion')  # it returns true or false
print(res)

#find()
res = str.find('Bit')
print(res)

#index()
res = str.index('Bit')
print(res)

#isalnum()

res = str.isalnum()
print(res)

#isalpha
res = str.isalpha()
print(res)

#isdigit()

res = str.isdigit()
print(res)


#islower()
res = str.islower()
print(res)


#isspace()

res = str.isspace()
print(res)

# calculte sapces in given string
str1 = 'FirstBit   Solution'
count = 0
for char in str1:
    if char.isspace():
        count +=1

print(count)


#isupper()
res = str.isupper()
print(res)

#join()

li = ['a','b','c']
res = ' , '.join(li)
print(res)


#lower()
res = str.lower()
print(res)


#split()
str.split()
print(res)

#replace()
res = str.replace('Bit','Byte')
print(res)

#startswith()
res = str.startswith('Fir')
print(res)

#strip()
str2 = "['127.0.0.1']"
res = str2.strip("'[]'")
print(res)


# swapcase()   ---- convert uppercase to lowercase and lowercase to uppercase
res = str.swapcase()
print(res)

#title()
res = str.title()
print(res)
