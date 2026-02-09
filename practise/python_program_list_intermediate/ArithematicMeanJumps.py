def arithmetic_mean_jumps(n):
    steps = 0
    seen = set()  # To detect oscillation

    while n >= 10 and n not in seen:
        seen.add(n)
        digits = [int(d) for d in str(n)]
        n = sum(digits) // len(digits)  # Arithmetic mean (integer division)
        steps += 1

    return steps, n  # Returns number of steps and the final stable value

# Example usage
num = 9875
steps, result = arithmetic_mean_jumps(num)
print(f"Arithmetic mean jumps for {num}: {steps} jumps, final value: {result}")
