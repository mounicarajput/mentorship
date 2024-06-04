#https://leetcode.com/problems/score-of-a-string/
"""You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.
Example 1:
Input: s = "hello"
Output: 13

Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:
Input: s = "zaz"
Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

 Constraints:
2 <= s.length <= 100
s consists only of lowercase English letters."""


class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        # Iterate over all indices from 0 to the second-to-last index
        # Calculate and accumulate the absolute difference of ASCII values
        # between adjacent characters
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score

# Create an instance of Solution
solution = Solution()

# Example 1
s1 = "hello"
print(solution.scoreOfString(s1))

# Example 2
s2 = "zaz"
print(solution.scoreOfString(s2))

