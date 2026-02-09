def second_lowest_greatest(arr):
    if len(arr) < 2:
        return "List must have at least 2 elements"

    arr = sorted(set(arr))  # Sort and remove duplicates
    return arr[1], arr[-2]  # Second smallest and second largest

# Example usage
nums = [10, 20, 4, 45, 99, 30]
print(second_lowest_greatest(nums))  # Output: (10, 45)
