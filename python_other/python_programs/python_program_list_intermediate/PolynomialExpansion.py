def binomial_expand(a, b, n):
    from math import comb  # Combination formula
    terms = [(comb(n, k) * (a ** (n - k)) * (b ** k)) for k in range(n + 1)]
    return terms

# Example: (x + 1)^3
coefficients = binomial_expand(1, 1, 3)
print(coefficients)  # Output: [1, 3, 3, 1]
