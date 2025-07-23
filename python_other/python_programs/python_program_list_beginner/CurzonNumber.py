def is_curzon_number(n):
    power_term = 2 ** n + 1
    product_term = 2 * n + 1
    return power_term % product_term == 0

# Test the function
number = int(input("Enter a number: "))
if is_curzon_number(number):
    print(f"{number} is a Curzon number.")
else:
    print(f"{number} is not a Curzon number.")