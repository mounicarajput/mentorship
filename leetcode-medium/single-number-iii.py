
class Solution:
    def singleNumber(self, nums):
        count= {}
        for num in nums:
            if num not in count:
                count[num ]=1
            else:
                count [num ]+=1
        return[key for key, value in count.items( )if value==1]
# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 1, 3, 2, 5]
print(solution.singleNumber(nums1))  # Output: [3, 5] or [5, 3]

# Example 2
nums2 = [-1, 0]
print(solution.singleNumber(nums2))  # Output: [-1, 0]




