def NonrepeatingCharacter(str):
    char_count = {}

    # Count occurrences of each character
    for char in str:
        if char != " ":  # Ignore spaces
            char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for char in str:
        if char != " " and char_count[char] == 1:
            return char  # Return immediately when found

# Example Test Cases
print(NonrepeatingCharacter("abcdef"))  # Output: a
print(NonrepeatingCharacter("hello world hi hey"))  # Output: w
print(NonrepeatingCharacter("agettkgaeee"))  # Output: k
