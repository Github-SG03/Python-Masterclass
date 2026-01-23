def generate_brackets(n, open_count=0, close_count=0, current_string="", result=None):
    if result is None:
        result = []

    # Base Case: When the length of the current string reaches 2 * n
    if len(current_string) == 2 * n:
        result.append(current_string)
        return

    # Add an opening bracket if we haven't used all
    if open_count < n:
        generate_brackets(n, open_count + 1, close_count, current_string + "(", result)

    # Add a closing bracket if it doesn't exceed open brackets
    if close_count < open_count:
        generate_brackets(n, open_count, close_count + 1, current_string + ")", result)

    return result

# Example Usage
n = 3
combinations = generate_brackets(n)
print(f"Valid bracket combinations for n={n}:")
print(combinations)
