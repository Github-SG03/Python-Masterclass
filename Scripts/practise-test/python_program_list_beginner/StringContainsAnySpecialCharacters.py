import re

def contains_special_characters(s):
    # Define a regex pattern for special characters
    pattern = re.compile('[^a-zA-Z0-9]')
    # Search for the pattern in the string
    if pattern.search(s):
        return True
    return False

# Test the function
test_string = "Hello@World!"
print(f"Does the string '{test_string}' contain special characters? {contains_special_characters(test_string)}")