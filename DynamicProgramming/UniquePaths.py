# LeetCode 62. Unique Paths
# Difficulty: Medium
#
# Problem: A robot starts at the top-left corner of an m x n grid and
# wants to reach the bottom-right corner. It can only move right or down.
# Return the number of unique paths.
#
# Approach: Dynamic programming (top-down / memoization). The number of
# ways to reach cell (x, y) is the sum of the ways to reach the cell above
# (x-1, y) and the cell to the left (x, y-1). Cells in the first row or
# first column can only be reached one way (straight along the edge).
# We start the recursion at the destination (m-1, n-1) and cache every
# computed cell in the matrix so each cell is solved only once.
#
# Time complexity: O(m * n) - each cell is computed once, then reused
# Space complexity: O(m * n) - matrix of results, plus recursion stack
#                    up to O(m + n) deep

class Solution:

    def calculate(self, x, y, matrix):

        # Already computed (0 means "not yet visited", since every
        # reachable cell has at least 1 path) - return the cached value
        if matrix[x][y] != 0:
            return matrix[x][y]

        # Top row: can only arrive from the left
        elif x == 0:
            matrix[x][y] = self.calculate(x, y-1, matrix)
            return matrix[x][y]
        # Left column: can only arrive from above
        elif y == 0:
            matrix[x][y] = self.calculate(x-1, y, matrix)
            return matrix[x][y]

        # Interior cell: paths from above + paths from the left
        matrix[x][y] = self.calculate(x-1, y, matrix) + self.calculate(x, y-1, matrix)
        return matrix[x][y]


    def uniquePaths(self, m: int, n: int) -> int:

        matrix = [[0 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 1  # base case: one way to be at the start
        return self.calculate(m-1, n-1, matrix)



if __name__ == "__main__":

    solution = Solution()
    print(solution.uniquePaths(3, 7))