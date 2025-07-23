def DistinctCharacters(s):
    # Use a set to store distinct characters
    unique_chars = set(s)
    
    # Check if there are at least 10 distinct characters
    return "true" if len(unique_chars) >= 10 else "false"

# Test cases
print(DistinctCharacters("abc123kkmmmm?"))  # Output: "false"
print(DistinctCharacters("12334bbmma:=6"))  # Output: "true"
print(DistinctCharacters("eeeemmmmmmmmm1000"))  # Output: "false"
