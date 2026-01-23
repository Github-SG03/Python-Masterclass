def longest_consecutive(arr):
    # If array has less than 4 elements, return sum
    if len(arr) < 4:
        return sum(arr)

    num_set = set(arr)  # Store all numbers in a set for fast lookup
    max_length = 0

    for num in num_set:
        # If it's a sequence start (previous number doesn't exist)
        if num - 1 not in num_set:
            current_length = 1
            current_num = num

            # Expand the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# Example Test Cases
print(longest_consecutive([6, 7, 3, 1, 100, 102, 6, 12]))  # Output: 2
print(longest_consecutive([5, 6, 1, 2, 8, 9, 7]))  # Output: 5
print(longest_consecutive([4, 3, 8, 1, 2, 6, 100, 9]))  # Output: 4
print(longest_consecutive([1, 2, 3]))  # Output: 6 (sum of 1+2+3)
