def is_happy_number(n):
    def get_next(number):
        return sum(int(char) ** 2 for char in str(number))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1

# Example usage
number = 19
if is_happy_number(number):
    print(f"{number} is a happy number.")
else:
    print(f"{number} is not a happy number.")