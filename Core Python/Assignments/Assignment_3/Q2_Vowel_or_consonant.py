#2. Write a program to input any alphabet and check whether it is vowel or consonant.

text = input("Enter Alphabet: ")

if text in 'aeiouAEIOU':
    print(f"{text} is Vowel")

else:
    print(f"{text} is consonant")
