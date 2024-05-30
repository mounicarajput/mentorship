""""Given the head of a singly linked list, reverse the list, and return the reversed list.

 Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:
Input: head = [1,2]
Output: [2,1]


Example 3:
Input: head = []
Output: []


Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

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

# Helper function to convert a linked list back to a list of values
def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Test 1
    test = [1, 2, 3, 4, 5]
    head = create_linked_list(test)
    reversed_head = solution.reverseList(head)
    print(linked_list_to_list(reversed_head))  # Output: [5, 4, 3, 2, 1]

    # Test 2
    test = [1, 2]
    head = create_linked_list(test)
    reversed_head = solution.reverseList(head)
    print(linked_list_to_list(reversed_head))  # Output: [2, 1]

    # Test 3
    test = []
    head = create_linked_list(test)
    reversed_head = solution.reverseList(head)
    print(linked_list_to_list(reversed_head))  # Output: []












