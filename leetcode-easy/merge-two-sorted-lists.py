"""" Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""""

#solution:
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b


#Merge Two 2D Arrays by Summing Values
from collections import defaultdict

def mergeArrays(nums1, nums2):
    merged = defaultdict(int)
    for id, val in nums1 + nums2:
        merged[id] += val
    return sorted(merged.items())

# Example usage:
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(mergeArrays(nums1, nums2))  # Output: [(1, 6), (2, 3), (3, 2), (4, 6)]
