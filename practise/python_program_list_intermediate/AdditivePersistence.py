def additive_persistence(n):
    count = 0
    while n >= 10:  # Repeat until single digit is reached
        n = sum(int(digit) for digit in str(n))  # Sum of digits
        count += 1
    return count

# Example usage
num = 9875
result = additive_persistence(num)
print(f"Additive persistence of {num} is {result}")
