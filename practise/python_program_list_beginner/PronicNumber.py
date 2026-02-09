def is_pronic_number(num):
    for i in range(int(num**0.5) + 1):
        if i * (i + 1) == num:
            return True
    return False

def generate_pronic_numbers(limit):
    pronic_numbers = []
    for i in range(limit + 1):
        pronic_numbers.append(i * (i + 1))
    return pronic_numbers

if __name__ == "__main__":
    limit = 100  # You can change the limit as needed
    pronic_numbers = generate_pronic_numbers(limit)
    print(f"Pronic numbers up to {limit}: {pronic_numbers}")
    
    # Example to check if a number is pronic
    number_to_check = 20
    if is_pronic_number(number_to_check):
        print(f"{number_to_check} is a pronic number.")
    else:
        print(f"{number_to_check} is not a pronic number.")