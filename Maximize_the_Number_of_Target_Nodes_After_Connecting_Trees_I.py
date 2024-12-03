"""
3372. Maximize the Number of Target Nodes After Connecting Trees I
Medium
There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

Output: [9,7,9,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 0 from the second tree.
For i = 2, connect node 2 from the first tree to node 4 from the second tree.
For i = 3, connect node 3 from the first tree to node 4 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

Output: [6,3,3,3,3]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.

Constraints:

2 <= n, m <= 1000
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
0 <= k <= 1000
"""
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        g1, g2 = defaultdict(list),defaultdict(list)
        for x,y in edges1:
            g1[x].append(y)
            g1[y].append(x)
        for x,y in edges2:
            g2[y].append(x) 
            g2[x].append(y)
        seen1,seen2 = set(),set()

        def find1(node, val):
            ans = 0
            seen1.add(node)
            if not val:
                return 0
            else:
                for adj in g1[node]:
                    if adj in seen1:
                        continue
                    ans += find1(adj, val - 1) + 1
            return ans
            
        def find2(node, val):
            ans = 0
            seen2.add(node)
            if not val:
                return 0
            else:
                for adj in g2[node]:
                    if adj in seen2:
                        continue
                    ans += find2(adj, val - 1) + 1
            return ans

        res, curr, g2max = [],0,0
        for key in g2.keys():
            g2max = max(g2max,find2(key, k - 1) + 1)
            seen2.clear()
        g2max = 1 if k == 0 else g2max
        for key in range(len(edges1) + 1):
            if k > 0:
                curr = find1(key, k) + 1
                seen1.clear()
            res.append(curr + g2max)
        return res
