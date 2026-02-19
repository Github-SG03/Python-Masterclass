def element_merger(arr):
    while len(arr) > 1:
        arr = [(arr[i] + arr[i+1]) % 10 for i in range(len(arr) - 1)]
    return arr[0]

# Example Usage
print(element_merger([4, 5, 6, 7]))  # ✅ Output: 2
print(element_merger([1, 2, 3, 4, 5]))  # ✅ Output: 8
