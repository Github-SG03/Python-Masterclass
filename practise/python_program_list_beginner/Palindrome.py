# Palindrome Number Program in Python
def is_palindrome(number):
    """
    This function checks if a given number is a palindrome.
    
    A palindrome is a number that reads the same backward as forward.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    # Convert the number to a string
    str_number = str(number)
    
    # Reverse the string
    reversed_str_number = str_number[::-1]
    
    # Check if the original string is equal to the reversed string
    return str_number == reversed_str_number

# Example usage
if __name__ == "__main__":
    test_number = 121
    if is_palindrome(test_number):
        print(f"{test_number} is a palindrome.")
    else:
        print(f"{test_number} is not a palindrome.")
        