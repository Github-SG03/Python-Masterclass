def third_greatest(nums):
    if len(nums) < 3:
        return "List must have at least 3 numbers"
    
    nums = sorted(nums, reverse=True)  # Sort in descending order
    return nums[2]  # Third greatest element

# Example usage
arr = [10, 20, 4, 45, 99, 30]
print(third_greatest(arr))  # Output: 30
