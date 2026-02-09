def uncommon_words(str1, str2):
    # Split the strings into words
    words1 = str1.split()
    words2 = str2.split()
    
    # Create dictionaries to count the frequency of each word
    freq1 = {}
    freq2 = {}
    
    for word in words1:
        freq1[word] = freq1.get(word, 0) + 1
    
    for word in words2:
        freq2[word] = freq2.get(word, 0) + 1
    
    # Find uncommon words
    uncommon = []
    
    for word in freq1:
        if freq1[word] == 1 and word not in freq2:
            uncommon.append(word)
    
    for word in freq2:
        if freq2[word] == 1 and word not in freq1:
            uncommon.append(word)
    
    return uncommon

# Example usage
str1 = "apple banana mango"
str2 = "banana orange mango"
print(uncommon_words(str1, str2))  # Output: ['apple', 'orange']