def is_superincreasing(arr):
    total = 0  # Stores sum of previous elements
    for num in arr:
        if num <= total:
            return False  # Not superincreasing
        total += num  # Update sum
    return True

# Example usage
print(is_superincreasing([1, 2, 6, 13, 27]))  # ✅ True
print(is_superincreasing([1, 3, 4, 7, 9]))    # ❌ False
