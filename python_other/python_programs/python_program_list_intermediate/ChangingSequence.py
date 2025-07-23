def changing_sequence(arr):
    if len(arr) < 2:
        return -1  # No change possible
    
    for i in range(len(arr) - 1):
        if (arr[i] < arr[i + 1]):  # Increasing
            increasing = True
        elif (arr[i] > arr[i + 1]):  # Decreasing
            increasing = False
        else:
            continue  # Ignore equal elements
        
        # Check for change in pattern
        if i > 0 and ((arr[i - 1] < arr[i]) != increasing):
            return i
    
    return -1  # No change detected

# Example Usage
print(changing_sequence([1, 2, 3, 4, 3, 2, 1]))  # ✅ Output: 3
print(changing_sequence([10, 9, 8, 7, 8, 9]))    # ✅ Output: 3
print(changing_sequence([1, 2, 3, 4, 5]))        # ✅ Output: -1 (No change)
