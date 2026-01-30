# Create a function check_positive(n) that checks whether a number is positive or negative.

def check_positive(n):
    print(f"{n} is", 'positive' if n > 0 else 'negative' if n < 0 else 'Zero')

check_positive(1)
check_positive(-1)
check_positive(0)