# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

d1 = {'id':101,'name':"sujata",'salary':25000}

print(d1)

key = input("Enter to search key: ")

if key in d1:
    print('Key Exists')

else:
    print("Key not exists")
