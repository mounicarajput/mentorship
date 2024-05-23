"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:
Input: [1, 7, 11, 15] target = 8
Output: [0, 1]

Example 2:
Input: [3, 2, 4, 1] target = 5
Output: [0, 1]

Example 3:
Input: [3, 3] target = 9
Output: None

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?"""
#solution
def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

# Test cases
nums1 = [1, 7, 11, 15]
target1 = 8
print("Example 1:")
print("Input:", nums1, "target =", target1)
print("Output:", two_sum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4, 1]
target2 = 5
print("\nExample 2:")
print("Input:", nums2, "target =", target2)
print("Output:", two_sum(nums2, target2))  # Output: [0, 1]

nums3 = [3, 3]
target3 = 9
print("\nExample 3:")
print("Input:", nums3, "target =", target3)
print("Output:", two_sum(nums3, target3))  # Output: [0, 1]





