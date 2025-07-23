def word_split(strArr):
    word = strArr[0]  # The word to be split
    dictionary = set(strArr[1].split(","))  # Convert dictionary to a set for fast lookup

    # Try every possible split position
    for i in range(1, len(word)):  
        first_part = word[:i]  
        second_part = word[i:]

        # Check if both parts exist in the dictionary
        if first_part in dictionary and second_part in dictionary:
            return f"{first_part},{second_part}"

    return "not possible"

# Example Usage
print(word_split(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]))  # Output: "base,ball"
print(word_split(["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]))  # Output: "abcg,efd"
print(word_split(["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]))  # Output: "hello,cat"
print(word_split(["abcdef", "ab,cd,ef,xyz"]))  # Output: "not possible"
