def LetterChanges(str):
    # Define vowels for capitalization
    vowels = "aeiou"
    
    # Step 1: Shift each letter to the next in the alphabet
    shifted_str = ""
    for char in str:
        if char.isalpha():
            # Shift letter (handling 'z' -> 'a')
            new_char = chr(ord(char) + 1) if char != 'z' and char != 'Z' else 'a' if char == 'z' else 'A'
            # Capitalize vowels
            new_char = new_char.upper() if new_char in vowels else new_char
            shifted_str += new_char
        else:
            shifted_str += char  # Keep non-letter characters unchanged

    return shifted_str

# Test cases
print(LetterChanges("hello*3"))      # Output: Ifmmp*3
print(LetterChanges("fun times!"))   # Output: gvO Ujnft!
print(LetterChanges("abcdz"))        # Output: bcdeA
print(LetterChanges("XYZ"))          # Output: YZA
