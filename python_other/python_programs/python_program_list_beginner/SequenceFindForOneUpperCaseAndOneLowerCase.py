import re

def findSequence(text):
      # regex pattern
    pattern = '[A-Z][a-z]+'
    
    # Use re.search to find any match
    if re.search(pattern, text):
        return 'Yes'
    else:
        return 'No'

# Driver program
if __name__ == "__main__":
    word = 'geeAkAA55of55gee4ksabc3Ar2x'
    print(findSequence(word))
    word = 'Geeks'
    print(findSequence(word))
    word = 'geeksforgeeks'
    print(findSequence(word))