def max_subarray(arr):
    max_sum = float('-inf')  # Start with the smallest possible value
    current_sum = 0  # Current subarray sum

    for num in arr:
        current_sum += num  # Add current element to subarray sum
        max_sum = max(max_sum, current_sum)  # Update max sum
        if current_sum < 0:
            current_sum = 0  # Reset if sum is negative

    return max_sum  # Return the maximum subarray sum

# Example Usage
print(max_subarray([1, -2, 0, 3]))  # Output: 3
print(max_subarray([3, -1, -1, 4, 3, -1]))  # Output: 8
print(max_subarray([-2, 5, -1, 7, -3]))  # Output: 11
