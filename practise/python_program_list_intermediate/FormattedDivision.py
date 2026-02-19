def FormattedDivision(num1, num2):
    # Perform the division
    result = num1 / num2

    # Format the number with commas and 4 decimal places
    formatted_result = f"{result:,.4f}"

    return formatted_result

# Test cases
print(FormattedDivision(2, 3))          # Output: "0.6667"
print(FormattedDivision(10, 10))        # Output: "1.0000"
print(FormattedDivision(123456789, 10000))  # Output: "12,345.6789"
print(FormattedDivision(101, 2))        # Output: "50.5000"
