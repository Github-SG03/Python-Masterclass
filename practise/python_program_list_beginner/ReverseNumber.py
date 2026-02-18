def reverse_number(n):
    reversed_num = 0
    while n > 0:
        remainder = n % 10
        reversed_num = (reversed_num * 10) + remainder
        n = n // 10
    return reversed_num

# Example usage
number = 12345
print(f"The reverse of {number} is {reverse_number(number)}")