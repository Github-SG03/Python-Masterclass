def is_niven_number(num):
    # Calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    return num % sum_of_digits == 0

# Test the function
number = int(input("Enter a number: "))
if is_niven_number(number):
    print(f"{number} is a Niven number.")
else:
    print(f"{number} is not a Niven number.")