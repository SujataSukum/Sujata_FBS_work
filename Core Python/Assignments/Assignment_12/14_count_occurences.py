# 14. Python Program to count the occurrences of each word in a string.

s = input("Enter a string: ")

words = s.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for w in word_count:
    print(w, "--", word_count[w])
