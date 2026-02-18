import re

def CamelCase(str):
    # Split the string by any non-alphabetic characters
    words = re.split(r'[^a-zA-Z]', str)

    # Convert the first word to lowercase and capitalize the rest
    camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:] if word)

    return camel_case

# Test cases
print(CamelCase("BOB loves-coding"))  # Output: "bobLovesCoding"
print(CamelCase("cats AND*Dogs-are Awesome"))  # Output: "catsAndDogsAreAwesome"
print(CamelCase("a b c d-e-f%g"))  # Output: "aBCDEFG"
print(CamelCase("Hello_World-Example"))  # Output: "helloWorldExample"
