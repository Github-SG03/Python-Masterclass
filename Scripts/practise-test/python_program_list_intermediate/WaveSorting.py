def wave_sort_inplace(arr):
    n = len(arr)
    
    for i in range(n):
        # If at an even index and smaller than the previous element, swap
        if i > 0 and i % 2 == 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

        # If at an odd index and greater than the previous element, swap
        if i > 0 and i % 2 == 1 and arr[i] > arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

# Example usage
arr = [10, 90, 49, 2, 1, 5, 23]
wave_sort_inplace(arr)
print("Wave sorted array:", arr)
