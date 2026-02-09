# JUST FOR FUN
# ENTER ANY STRING AND RETURN JUST THE NUMBER

string1 = input("Enter any string: ")
final_val = str()

number = '1234567890'

for i in string1:
    if i in number:
        final_val += i

print(f"Returning : {int(final_val)}")