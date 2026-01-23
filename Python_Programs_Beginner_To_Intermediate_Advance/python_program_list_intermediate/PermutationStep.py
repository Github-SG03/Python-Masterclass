def PermutationStep(num):
    # Convert the number to a list of digits
    digits = list(str(num))
    
    # Find the first digit from the right that is smaller than the one after it
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # If no such digit is found, no greater permutation exists
    if i == -1:
        return -1

    # Find the smallest digit on the right side of i that is larger than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]
    
    # Reverse the order of the digits after index i
    digits = digits[:i+1] + sorted(digits[i+1:])
    
    # Convert back to integer and return
    return int("".join(digits))

# Test cases
print(PermutationStep(123))       # Output: 132
print(PermutationStep(12453))     # Output: 12534
print(PermutationStep(11121))     # Output: 11211
print(PermutationStep(41352))     # Output: 41523
print(PermutationStep(897654321)) # Output: 912345678
print(PermutationStep(76666666))  # Output: -1
