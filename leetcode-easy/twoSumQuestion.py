"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:
Input: [2, 7, 11, 15] target = 9
Output: [0, 1]

Example 2:
Input: [3, 7, 4, 1] target = 5
Output: [0, 1]

Example 3:
Input: [3, 3] target = 6
Output: None

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?"""
#solution

def twosum (nums,target):
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            if target - nums[i]==nums[j]:
                return [i,j]
    return None
test =[2,7,11,15]
target=9
print(twosum(test,target))

test =[3, 7, 4, 1]
target = 5
print(twosum(test,target))

test =[2,8,6,7]
target = 14
print(twosum(test,target))








