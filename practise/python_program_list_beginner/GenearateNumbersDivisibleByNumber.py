def generate_divisible_numbers(divisor, limit):
    divisible_numbers = []
    for num in range(1, limit + 1):
        if num % divisor == 0:
            divisible_numbers.append(num)
    return divisible_numbers

# Example usage
divisor = 5
limit = 100
result = generate_divisible_numbers(divisor, limit)
print(f"Numbers divisible by {divisor} up to {limit}: {result}")


# Output
# Numbers divisible by 5 up to 100: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
