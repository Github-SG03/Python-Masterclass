from collections import Counter

def mean_mode(arr):
    # Compute Mean
    mean_val = sum(arr) / len(arr)

    # Compute Mode
    freq = Counter(arr)
    max_count = max(freq.values())

    mode_values = [key for key, val in freq.items() if val == max_count]

    # If all values occur once, there's no mode
    mode_val = mode_values[0] if len(mode_values) == 1 else "No mode (Multiple modes or unique values)"

    return mean_val, mode_val

# Example Usage
arr = [1, 2, 2, 3, 4]
print(mean_mode(arr))  # ✅ Output: (2.4, 2)

arr = [1, 2, 3, 4, 5]
print(mean_mode(arr))  # ✅ Output: (3.0, "No mode (Multiple modes or unique values)")
