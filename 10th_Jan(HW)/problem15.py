# Write a function named print_table(n) that prints the multiplication table of a given number.

def print_table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
    print("\nDone")

table_val = int(input("Which number's table you want to print: "))
print(f"\nTable of {table_val}\n")
print_table(table_val)