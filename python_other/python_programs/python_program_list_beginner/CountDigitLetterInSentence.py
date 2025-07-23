def count_letters_and_digits(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return letters, digits

# Example usage
sentence = "Hello World! 123"
letters, digits = count_letters_and_digits(sentence)
print(f"Letters: {letters}, Digits: {digits}")

# Output
# Letters: 10, Digits: 3


