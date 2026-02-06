def split_and_join_string(input_string):
    # Split the string by spaces
    split_string = input_string.split()
    
    # Join the split string with hyphens
    joined_string = '-'.join(split_string)
    
    return joined_string

# Example usage
if __name__ == "__main__":
    input_string = "This is a sample string"
    result = split_and_join_string(input_string)
    print(result)  # Output: This-is-a-sample-string