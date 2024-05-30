# Question: https://leetcode.com/problems/palindrome-number/

"""Given an integer x, return true if x is a
palindrome
, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1

"""
# Solution:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Convert the number to a string and check if it reads the same backward
        str_x = str(x)
        return str_x == str_x[::-1]


# Example usage
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
print(solution.isPalindrome(12321))



#https://leetcode.com/problems/palindrome-linked-list

"""Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example1:
Input: head = [1, 2, 2, 1]
Output: true

Example2:
Input: head = [1, 2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 Follow up: Could you do it in O(n) time and O(1) space?"""

# Helper function to create linked list from a list of values

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = ''
        while head:
            res += str(head.val)
            head = head.next

        return res == res[::-1]


# Helper function to create linked list from a list of values
def create_linked_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Example usage:
vals = [1, 2, 2, 1]  # Example input
head = create_linked_list(vals)
sol = Solution()
print(sol.isPalindrome(head))  # Output: True

vals = [1, 2]  # Another example input
head = create_linked_list(vals)
sol = Solution()
print(sol.isPalindrome(head))  # Output: False


