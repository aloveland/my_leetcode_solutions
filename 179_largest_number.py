"""179. Largest Number
Medium
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.


Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isend = defaultdict(int)
        self.count = defaultdict(int)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        start = TrieNode()
        totalLen = 0
        for i, n in enumerate(nums):
            node = start
            for c in str(n):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node.count[c] += 1
                node = node.children[c]
                totalLen += 1
            node.isend[str(n)[-1]] += 1
        res = -inf
        numAtIndex = {}
        def dfs(x, node, number):
            nonlocal res
            intnum = int(number) if number else 0
            if x in numAtIndex and intnum < numAtIndex[x]:
                return 
            numAtIndex[x] = intnum
            if x >= totalLen:
                res = int(number)
                return
            last = number[-1] if number else None
            for i in range(9,-1,-1):
                curr = str(i)
                if curr in node.children and node.count[curr] > 0:
                    node.count[curr] -= 1
                    dfs(x + 1, node.children[curr], number + curr)
                    node.count[curr] += 1
                if node.isend[last] > 0 and curr in start.children and start.count[curr] > 0:
                    start.count[curr] -= 1
                    node.isend[last] -= 1
                    dfs(x + 1, start.children[curr], number + curr)
                    node.isend[last] += 1
                    start.count[curr] += 1
        dfs(0,start, "")
        return str(res)