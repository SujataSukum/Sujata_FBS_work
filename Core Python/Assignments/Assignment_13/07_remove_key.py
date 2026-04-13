# 7. Python Program to Remove the Given Key from a Dictionary

d = {"id": 101, "name": "Sujata", "salary": 50000}

key = input("Enter key to remove: ")

if key in d:
    del d[key]
    print("Updated dictionary:", d)
else:
    print("Key not found")
