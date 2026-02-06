def array_addition(arr):
    target = max(arr)  # Step 1: Find the largest number
    arr.remove(target)  # Step 2: Remove it from the array
    
    n = len(arr)
    dp = {0}  # Stores sums that can be formed
    
    for num in arr:
        new_sums = {num + x for x in dp}  # Add current num to all previous sums
        dp.update(new_sums)  # Merge new sums

    return "true" if target in dp else "false"

# Example Usage
print(array_addition([5, 7, 16, 1, 2]))  # Output: "false"
print(array_addition([3, 5, -1, 8, 12])) # Output: "true"
print(array_addition([4, 6, 23, 10, 1, 3])) # Output: "true"
