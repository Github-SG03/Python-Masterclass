def count_digits(n):
    """
    Count the number of digits in a number.
    
    Parameters:
    n (int): The number to count digits of.
    
    Returns:
    int: The number of digits in n.
    """
    count_digits = 0
    x = n
    while x:
        x = x // 10
        count_digits += 1
    return count_digits

def is_disarium(n):
    """
    Check if a number is a Disarium number.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is a Disarium number, False otherwise.
    """
    count_digit = count_digits(n)
    sum_of_powers = 0
    x = n
    while x:
        r = x % 10
        sum_of_powers += r ** count_digit
        x = x // 10
        count_digit -= 1
    return sum_of_powers == n

# Example usage
if __name__ == "__main__":
    test_number = 89
    if is_disarium(test_number):
        print(f"{test_number} is a Disarium number.")
    else:
        print(f"{test_number} is not a Disarium number.")
