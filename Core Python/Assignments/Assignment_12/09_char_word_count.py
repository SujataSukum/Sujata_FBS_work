# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

s = input("Enter the string: ")

chr_count = len(s)

word_count = 1

for ch in s:
    if ch == " ":
        word_count += 1

print("Total Words are in string: ",word_count)
print("Total characters are in string: ",chr_count)


