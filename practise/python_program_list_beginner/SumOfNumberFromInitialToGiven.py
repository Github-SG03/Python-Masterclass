# File: sum_of_numbers.py

def calculate_sum(n):
    return sum(range(1, n + 1))

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The sum of all numbers from 1 to {n} is {calculate_sum(n)}")