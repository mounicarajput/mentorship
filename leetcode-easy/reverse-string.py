#https://leetcode.com/problems/reverse-string/
"""Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character."""

#solution

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]
        # Move pointers towards the center
        left += 1
        right -= 1

# Example usage
s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
