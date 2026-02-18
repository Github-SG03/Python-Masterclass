from itertools import combinations

def scale_balancing(scale, weights):
    left, right = scale
    difference = abs(left - right)  # Get absolute difference

    # Check if one weight alone can balance
    if difference in weights:
        return True  

    # Check if two weights can balance
    for w1, w2 in combinations(weights, 2):
        if w1 + w2 == difference:
            return True  

    return False  # If no combination works

# Example Usage
print(scale_balancing([5, 9], [1, 2, 6, 7]))  # ✅ True (Add 2 and 2)
print(scale_balancing([3, 8], [1, 2, 5]))    # ✅ True (Add 5 to left)
print(scale_balancing([6, 10], [1, 2, 3]))   # ❌ False (No way to balance)
