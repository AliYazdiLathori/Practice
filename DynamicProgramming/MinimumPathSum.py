# LeetCode 64. Minimum Path Sum
# Difficulty: Medium
#
# Problem: Given an m x n grid filled with non-negative numbers, find a
# path from the top-left to the bottom-right corner that minimizes the
# sum of all numbers along the path. You can only move right or down.
#
# Approach: Dynamic programming (top-down / memoization). The cheapest
# cost to reach cell (x, y) is its own value plus the cheaper of the two
# cells that can lead into it: the one above (x-1, y) or the one to the
# left (x, y-1). Cells in the first row or column have only one possible
# predecessor. We start at the destination, recurse backwards, and cache
# results in `cost` so each cell is computed only once.
#
# Time complexity: O(m * n) - each cell is computed once, then reused
# Space complexity: O(m * n) - cost matrix, plus recursion stack
#                    up to O(m + n) deep

class Solution:

    def calculate(self, x, y, grid, cost):

        # Already computed (-1 means "not yet visited", since 0 is a
        # valid cost) - return the cached value
        if cost[x][y] != -1:
            return cost[x][y]

        # Top row: can only arrive from the left
        elif x == 0:
            cost[x][y] = self.calculate(x, y-1, grid, cost) + grid[x][y]
            return cost[x][y]

        # Left column: can only arrive from above
        elif y == 0:
            cost[x][y] = self.calculate(x-1, y, grid, cost) + grid[x][y]
            return cost[x][y]

        # Interior cell: take the cheaper of (above, left), then add this cell's value
        cost[x][y] = min(self.calculate(x-1, y, grid, cost), self.calculate(x, y-1, grid, cost)) + grid[x][y]
        return cost[x][y]

    def minPathSum(self, grid: list[list[int]]) -> int:

        n = len(grid)     # number of rows
        m = len(grid[0])  # number of columns
        cost = [[-1 for _ in range(m)] for _ in range(n)]
        cost[0][0] = grid[0][0]  # base case: cost to reach the start is its own value

        return self.calculate(n-1, m-1, grid, cost)






if __name__ == "__main__":
    solution = Solution()
    print(solution.minPathSum([[1, 2, 3], [4, 5, 6]]))