def compute_word_frequency(text):
    words = text.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

if __name__ == "__main__":
    text = input("Enter some text: ")
    frequency = compute_word_frequency(text)
    
    for word, count in frequency.items():
        print(f"{word}: {count}")