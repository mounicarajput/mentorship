# Question : https://leetcode.com/problems/longest-palindromic-substring/

"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
"""
#Solution
def longestPalindrome(s):
    size = len(s)
    while size > 0:
        for i in range(len(s) - size + 1):
            x = s[i:i + size]
            if x == x[::-1]:
                return x
        size -= 1
    return ""

# Example usage
s1 = "babad"
print(longestPalindrome(s1))  # Output: "bab" or "aba"

s2 = "cbbd"
print(longestPalindrome(s2))  # Output: "bb"



