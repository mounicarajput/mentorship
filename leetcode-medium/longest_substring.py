# question : https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""

Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


#Solution

def longest_unique_substring(s):
    max_length = 0  # Initialize the maximum length of the substring
    start = 0  # Initialize the starting index of the current substring
    char_index = {}  # Create a dictionary to store the most recent index of each character

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Examples
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

output1 = longest_unique_substring(s1)
output2 = longest_unique_substring(s2)
output3 = longest_unique_substring(s3)

print(output1)  # Output: 3
print(output2)  # Output: 1
print(output3)  # Output: 3
