def PalindromicSubstring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the palindrome found

    longest_palindrome = ""

    for i in range(len(s)):
        # Check for odd-length palindrome
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest_palindrome):
            longest_palindrome = odd_palindrome
        
        # Check for even-length palindrome
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome

    return longest_palindrome if len(longest_palindrome) > 2 else "none"

# Test cases
print(PalindromicSubstring("abracecars"))  # Output: "racecar"
print(PalindromicSubstring("hellosannasmith"))  # Output: "sannas"
print(PalindromicSubstring("abcdefgg"))  # Output: "none"
print(PalindromicSubstring("abacdfgdcaba"))  # Output: "aba"
print(PalindromicSubstring("banana"))  # Output: "anana"
