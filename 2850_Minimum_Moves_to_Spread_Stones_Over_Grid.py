"""
2850. Minimum Moves to Spread Stones Over Grid
Medium

You are given a 0-indexed 2D integer matrix grid of size 3 * 3, representing the number of stones in each cell. The grid contains exactly 9 stones, and there can be multiple stones in a single cell.

In one move, you can move a single stone from its current cell to any other cell if the two cells share a side.

Return the minimum number of moves required to place one stone in each cell.

Example 1:


Input: grid = [[1,1,0],[1,1,1],[1,2,1]]
Output: 3
Explanation: One possible sequence of moves to place one stone in each cell is: 
1- Move one stone from cell (2,1) to cell (2,2).
2- Move one stone from cell (2,2) to cell (1,2).
3- Move one stone from cell (1,2) to cell (0,2).
In total, it takes 3 moves to place one stone in each cell of the grid.
It can be shown that 3 is the minimum number of moves required to place one stone in each cell.
Example 2:


Input: grid = [[1,3,0],[1,0,0],[1,0,3]]
Output: 4
Explanation: One possible sequence of moves to place one stone in each cell is:
1- Move one stone from cell (0,1) to cell (0,2).
2- Move one stone from cell (0,1) to cell (1,1).
3- Move one stone from cell (2,2) to cell (1,2).
4- Move one stone from cell (2,2) to cell (2,1).
In total, it takes 4 moves to place one stone in each cell of the grid.
It can be shown that 4 is the minimum number of moves required to place one stone in each cell.
 

Constraints:

grid.length == grid[i].length == 3
0 <= grid[i][j] <= 9
Sum of grid is equal to 9.
"""
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        fill,excess = [],[]
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    fill.append([i,j])
                elif grid[i][j] > 1:
                    excess.append([i,j])
        def dist(start,dest):
            return abs(start[0] - dest[0]) + abs(start[1] - dest[1])
        e,f = len(excess), len(fill)
        @cache
        def dp(x, mask):
            if x >= e:
                return 0
            ans = inf
            for i in range(f):
                if not(1 << i & mask):
                    src,dest = tuple(excess[x]), tuple(fill[i])
                    grid[excess[x][0]][excess[x][1]] -= 1
                    if grid[excess[x][0]][excess[x][1]] > 1:
                        ans = min(ans, dp(x, 1 << i | mask) + dist(src,dest))
                    else:
                        ans = min(ans, dp(x + 1, 1 << i | mask) + dist(src,dest))
                    grid[excess[x][0]][excess[x][1]] += 1
            return ans
        res = dp(0,0)
        dp.cache_clear()
        return res