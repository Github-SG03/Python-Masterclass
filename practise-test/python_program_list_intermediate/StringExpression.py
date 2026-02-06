def StringExpression(s):
    num_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    # Replace words with digits and operators
    expression = (s.replace("plus", "+")
                    .replace("minus", "-"))
    
    for word, digit in num_words.items():
        expression = expression.replace(word, digit)
    
    # Evaluate the mathematical expression
    result = eval(expression)

    # Convert result back to word format
    num_to_word = ["zero", "one", "two", "three", "four", "five", 
                   "six", "seven", "eight", "nine"]
    
    result_str = ''.join(num_to_word[int(digit)] for digit in str(abs(result)))
    
    return "negative" + result_str if result < 0 else result_str

# Test cases
print(StringExpression("foursixminustwotwoplusonezero")) # Output: "threefour"
print(StringExpression("onezeropluseight")) # Output: "oneeight"
print(StringExpression("oneminusoneone")) # Output: "negativeonezero"
print(StringExpression("seveneightplustwoone")) # Output: "nineeight"
print(StringExpression("fivezerominusfivezero")) # Output: "zero"
