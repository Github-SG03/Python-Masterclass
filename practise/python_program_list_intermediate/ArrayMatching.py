def array_matching(arr1, arr2):
    max_len = max(len(arr1), len(arr2))
    arr1 += [0] * (max_len - len(arr1))
    arr2 += [0] * (max_len - len(arr2))
    
    return [arr1[i] + arr2[i] for i in range(max_len)]

# Example Usage
print(array_matching([1, 2, 3], [4, 5, 6]))   # ✅ Output: [5, 7, 9]
print(array_matching([1, 2], [4, 5, 6]))      # ✅ Output: [5, 7, 6]
print(array_matching([1, 2, 3, 4], [2, 3]))   # ✅ Output: [3, 5, 3, 4]
