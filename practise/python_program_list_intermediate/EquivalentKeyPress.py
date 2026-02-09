def process_keystrokes(keystrokes):
    stack = []
    
    for key in keystrokes:
        if key != "<-":
            stack.append(key)  # Add character to stack
        elif stack:
            stack.pop()  # Remove last character on backspace
    
    return "".join(stack)  # Convert final stack to a string

def equivalent_keypress(seq1, seq2):
    return process_keystrokes(seq1) == process_keystrokes(seq2)

# Example Usage
seq1 = ["a", "b", "c", "<-", "d"]
seq2 = ["a", "b", "d"]

print(equivalent_keypress(seq1, seq2))  # Output: True
