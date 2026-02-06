def nearest_smaller_values(arr):
    stack = []  # Stack to keep track of previous smaller elements
    result = []  # Stores the nearest smaller values

    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()  # Remove elements that are greater than or equal

        if stack:
            result.append(stack[-1])  # Nearest smaller element
        else:
            result.append(-1)  # No smaller element found

        stack.append(num)  # Push current element onto stack

    return " ".join(map(str, result))  # Return space-separated string

# Example Usage
print(nearest_smaller_values([5, 3, 1, 9, 7, 3, 4, 1]))  # Output: -1 -1 -1 1 1 1 3 1
print(nearest_smaller_values([2, 4, 5, 1, 7]))  # Output: -1 2 4 -1 1
print(nearest_smaller_values([5, 2, 8, 3, 9, 12]))  # Output: -1 -1 2 2 3 9
