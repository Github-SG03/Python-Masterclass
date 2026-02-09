from itertools import product

def plus_minus(num):
    num_str = str(num)
    n = len(num_str)
    max_minus = -1
    best_expression = "not possible"

    # Generate all possible combinations of '+' and '-'
    for signs in product("+-", repeat=n-1):
        expression = num_str[0]  # Start with the first digit
        minus_count = 0

        # Build the expression
        for i in range(n-1):
            expression += signs[i] + num_str[i+1]
            if signs[i] == '-':
                minus_count += 1
        
        # Evaluate the expression
        if eval(expression) == 0:
            if minus_count > max_minus:
                max_minus = minus_count
                best_expression = "".join(signs)

    return best_expression

# Example Usage
print(plus_minus(35132))  # Output: -++-
print(plus_minus(26712))  # Output: -+--
print(plus_minus(199))    # Output: not possible
print(plus_minus(1234))   # Output: -++ (or another valid result)
