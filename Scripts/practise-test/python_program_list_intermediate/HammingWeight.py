def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print(count_ones(9))  # ✅ Output: 2 (0b1001 has two 1's)
