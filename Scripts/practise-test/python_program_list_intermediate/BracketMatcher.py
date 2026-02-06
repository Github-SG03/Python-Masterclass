def BracketMatcher(str):
    count = 0
    
    for char in str:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        # If count becomes negative, it means there's an unmatched closing bracket
        if count < 0:
            return 0

    # If count is 0, all brackets are correctly matched
    return 1 if count == 0 else 0

# Test cases
print(BracketMatcher("(coder)(byte))"))   # Output: 0
print(BracketMatcher("(c(oder)) b(yte)")) # Output: 1
print(BracketMatcher("((hello (world))")) # Output: 0
print(BracketMatcher("(hello (world))"))  # Output: 1
print(BracketMatcher("no brackets"))      # Output: 1
