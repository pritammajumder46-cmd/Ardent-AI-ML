# Count Vowels: Count vowels in a string using a dictionary

text = input("Enter a string: ").lower()

vowel_dict = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}

for i in text:
    if i in vowel_dict:
        vowel_dict[i] = vowel_dict[i] + 1

print(f"Vowels in the text is\n")
print(vowel_dict)