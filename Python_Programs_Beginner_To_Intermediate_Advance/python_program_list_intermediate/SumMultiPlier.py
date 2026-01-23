def sum_multiplier(arr):
    if len(arr) < 2:
        return False  # Need at least two elements

    total_sum = sum(arr)  # Compute sum of array
    max_product = max(arr[i] * arr[j] for i in range(len(arr)) for j in range(i+1, len(arr)))  # Find max product

    return (2 * total_sum) > max_product

# Example usage
print(sum_multiplier([2, 5, 8]))   # False
print(sum_multiplier([1, 2, 3]))   # True
print(sum_multiplier([3, 4, 5]))   # True
