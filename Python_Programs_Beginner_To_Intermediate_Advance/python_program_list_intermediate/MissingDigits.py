import re

def MissingDigit(equation):
    # Split equation into left and right sides of '='
    left, right = equation.split('=')
    left, right = left.strip(), right.strip()

    # Identify the operator in the left part
    match = re.search(r'(\d*x?\d*)\s*([\+\-\*/])\s*(\d*x?\d*)', left)
    
    if not match:
        return "Invalid input"
    
    # Extract operands and operator
    num1, operator, num2 = match.groups()

    # Convert right-hand side to an integer
    right_val = int(right)

    # Find the term with 'x'
    if 'x' in num1:
        missing_part = num1
        known_part = num2
        reverse = False
    elif 'x' in num2:
        missing_part = num2
        known_part = num1
        reverse = True
    else:
        missing_part = right
        known_part = eval(f"{num1} {operator} {num2}")
        reverse = False

    # Replace 'x' with digits 0-9 and check if equation holds
    for digit in range(10):
        candidate = missing_part.replace('x', str(digit))
        if candidate.isdigit():
            candidate = int(candidate)
            if operator == '+':
                valid = candidate + int(known_part) == right_val
            elif operator == '-':
                valid = (candidate - int(known_part) == right_val) if not reverse else (int(known_part) - candidate == right_val)
            elif operator == '*':
                valid = candidate * int(known_part) == right_val
            elif operator == '/':
                valid = (candidate / int(known_part) == right_val) if not reverse else (int(known_part) / candidate == right_val)

            if valid:
                return digit

    return "Not possible"

# Test cases
print(MissingDigit("3x + 12 = 46"))  # Output: 4
print(MissingDigit("4 - 2 = x"))     # Output: 2
print(MissingDigit("1x0 * 12 = 1200"))  # Output: 0
