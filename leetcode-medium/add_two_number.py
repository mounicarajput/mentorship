# Question : https://leetcode.com/problems/add-two-numbers/

# Solution
'''Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            current.next = ListNode(out)
            current = current.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return dummy.next


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to print the linked list
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))


# Example usage
if __name__ == "__main__":
    # Creating linked lists for the example
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    # Solution instance
    solution = Solution()

    # Adding the two numbers
    result = solution.addTwoNumbers(l1, l2)

    # Printing the result
    print_linked_list(result)
