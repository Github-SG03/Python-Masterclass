def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    
    distance = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            distance += 1
    
    return distance

# Example usage
str1 = "karolin"
str2 = "kathrin"
print(f"Hamming Distance: {hamming_distance(str1, str2)}")