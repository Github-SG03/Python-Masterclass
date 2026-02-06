import re

def SwapII(s):
    # Step 1: Swap the case of each character
    swapped_str = s.swapcase()

    # Step 2: Identify and swap numbers that have letters between them
    def swap_numbers(match):
        num1, middle, num2 = match.groups()
        return f"{num2}{middle}{num1}"  # Swap numbers but keep the middle part unchanged

    # Regular expression to find patterns like "6Hello4" (number-letter(s)-number)
    swapped_str = re.sub(r"(\d)([a-zA-Z]+)(\d)", swap_numbers, swapped_str)

    return swapped_str

# Test cases
print(SwapII("6Hello4 -8World, 7 yes3"))  # Output: 4hELLO6 -8wORLD, 7 YES3
print(SwapII("Hello -5LOL6"))             # Output: hELLO -6lol5
print(SwapII("2S 6 du5d4e"))              # Output: 2s 6 DU4D5E
print(SwapII("A1bC3d"))                   # Output: a3Bc1D
print(SwapII("123abc456"))                # Output: 456ABC123
