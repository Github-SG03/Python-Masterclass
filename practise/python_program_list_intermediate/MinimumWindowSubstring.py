from collections import Counter

def MinWindowSubstring(strArr):
    N, K = strArr  # Extract the two strings
    char_count = Counter(K)  # Frequency of characters in K

    left = 0
    min_length = float('inf')
    min_substring = ""
    required_chars = len(char_count)
    formed = 0
    window_counts = {}

    for right in range(len(N)):
        char = N[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in char_count and window_counts[char] == char_count[char]:
            formed += 1

        while formed == required_chars and left <= right:
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                min_substring = N[left:right + 1]

            left_char = N[left]
            window_counts[left_char] -= 1

            if left_char in char_count and window_counts[left_char] < char_count[left_char]:
                formed -= 1
            
            left += 1

    return min_substring

# Test cases
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))  # Output: "aksfaje"
print(MinWindowSubstring(["aaffhkksemckelloe", "fhea"]))   # Output: "affhkkse"
print(MinWindowSubstring(["aaabaaddae", "aed"]))           # Output: "dae"
print(MinWindowSubstring(["aabdccdbcacd", "aad"]))         # Output: "aabd"
