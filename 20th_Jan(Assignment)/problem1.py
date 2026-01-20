# Set Creation: Create a set of vowels from a given string

string1 = input("Enter a string: ").lower()

vowel_set = {'a','e','i','o','u'}
present_vowel_set = []

for i in string1:
    if i in vowel_set:
        present_vowel_set.append(i)

print(f"The set of vowels which are present in {string1.capitalize()} is :",set(present_vowel_set))
