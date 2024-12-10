"""
3381. Maximum Subarray Sum With Length Divisible by K
Medium
You are given an array of integers nums and an integer k.

Return the maximum sum of a non-empty subarray of nums, such that the size of the subarray is divisible by k.

A subarray is a contiguous non-empty sequence of elements within an array.

 
Example 1:

Input: nums = [1,2], k = 1

Output: 3

Explanation:

The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.

Example 2:

Input: nums = [-1,-2,-3,-4,-5], k = 4

Output: -10

Explanation:

The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.

Example 3:

Input: nums = [-5,1,2,-3,4], k = 2

Output: 4

Explanation:

The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.

 
Constraints:

1 <= k <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
"""
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix,t = {-1:0}, 0
        for i,v in enumerate(nums):
            t += v
            prefix[i] = t
        n = len(nums)
        res, best = -inf, {}
        for i in range(n - 1,-1,-1):
            if i + k - 1 < n:
                if n - k >= i + k:
                    best[i] = max(prefix[i + k - 1] - prefix[i - 1], prefix[i + k - 1] - prefix[i - 1] + best.get(i + k, -inf))
                else:
                    best[i] = prefix[i + k - 1] - prefix[i - 1]
                res = max(res, best[i])
            else:
                best[i] = nums[i]
        return res
            