#https://leetcode.com/problems/longest-palindrome/
"""Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only."""

#Solution

def longestPalindrome(s ) :
    from collections import Counter

    # Count the frequency of each character in the string
    char_count = Counter(s)

    # Initialize the length of the longest palindrome
    palindrome_length = 0
    has_odd = False

    # Iterate over character frequencies
    for count in char_count.values():
        if count % 2 == 0:
            palindrome_length += count
        else:
            palindrome_length += count - 1
            has_odd = True

    # If there is at least one character with an odd count, add one to the length for the center character
    if has_odd:
        palindrome_length += 1

    return palindrome_length


# Example usage
s1 = "abccccdd"
print(longestPalindrome(s1))  # Output: 7

s2 = "a"
print(longestPalindrome(s2))  # Output: 1
