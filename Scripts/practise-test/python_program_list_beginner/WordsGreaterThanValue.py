def words_greater_than_k(sentence, k):
    words = sentence.split()
    result = [word for word in words if len(word) > k]
    return result

# Example usage
sentence = "This is a sample sentence with some long words"
k = 4
print(words_greater_than_k(sentence, k))