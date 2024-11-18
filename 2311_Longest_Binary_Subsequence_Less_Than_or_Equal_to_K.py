"""
2311. Longest Binary Subsequence Less Than or Equal to K
Medium
You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
Example 2:

Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
 
Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= k <= 109
"""
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        prefix, z = [],0
        for c in s:
            prefix.append(z)
            if c == "0":
                z += 1
        prefix.append(prefix[-1])      
        n = len(bin(k)[2:])
        binaryk = list(bin(k)[2:])
        @cache
        def dp(x, length, over):
            if x < 0 or length >= n:
                return prefix[x + 1] if (not(over) or length < n) else -inf
            ans = 0
            if s[x] == "0":
                if binaryk[-(length + 1)] == "1":
                    ans = max(ans, dp(x - 1, length + 1, False) + 1)
                else:
                    ans = max(ans, dp(x - 1, length + 1, over) + 1)
            else:
                if binaryk[-(length + 1)] != "1":
                    ans = max(ans, dp(x - 1, length + 1, True) + 1)
                else:
                    ans = max(ans, dp(x - 1, length + 1, over) + 1)
            ans = max(ans, dp(x - 1, length, over))
            return ans
        res = dp(len(s) - 1, 0, False)
        dp.cache_clear()
        return res