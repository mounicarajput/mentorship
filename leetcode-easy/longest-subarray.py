"""""Longest Nice Subarray

You are given an array nums consisting of positive integers.
We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.
A subarray is a contiguous part of an array.
Note that subarrays of length 1 are always considered nice.

Example 1:
Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

Example 2:
Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.


Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109"""

def longestNiceSubarray(nums):
    lo, mask, ans = -1, 0, 1
    for hi, n in enumerate(nums):
        while (mask & n):  # n has duplicate set bits for current sliding window.
            lo += 1  # shrink left bound of current sliding window.
            mask ^= nums[lo]  # remove the corresponding element out of the window.
        mask |= n  # Expand right bound and put n into window.
        ans = max(ans, hi - lo)  # update the max window size.
    return ans
# Example usage:
nums1 = [1, 3, 8, 48, 10]
print(longestNiceSubarray(nums1))  # Output: 3

nums2 = [3, 1, 5, 11, 13]
print(longestNiceSubarray(nums2))  # Output: 1


def numSteps(s: str) -> int:
    steps = 0
    carry = 0  # Represents if we have an outstanding carry to add

    # Traverse the binary string from the least significant bit to the most significant bit
    for i in range(len(s) - 1, 0, -1):
        bit = s[i]
        if bit == '0':
            steps += 1 + carry  # If the bit is '0' and there's a carry, we had to add 1 first
        else:
            steps += 2 - carry  # If the bit is '1', we either just add 1 (if no carry) or we have already added and just divide
            carry = 1  # Generate a carry for the next significant bit

    return steps + carry  # Finally, add any remaining carry










