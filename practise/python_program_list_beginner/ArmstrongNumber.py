# ArmstrongNumber.py

# Function to check if a number is an Armstrong number
def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over each digit
    num_str = str(num)
    
    # Calculate the number of digits (order)
    num_digits = len(num_str)
    
    # Initialize the sum to 0
    sum_of_powers = 0
    
    # Iterate over each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer
        digit_int = int(digit)
        
        # Raise the digit to the power of the number of digits and add to the sum
        sum_of_powers += digit_int ** num_digits
    
    # Check if the sum of the powers is equal to the original number
    return sum_of_powers == num

# Main code to test the function
if __name__ == "__main__":
    # Test cases
    test_numbers = [153, 370, 371, 407, 9474, 9475]
    
    for number in test_numbers:
        if is_armstrong_number(number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")


