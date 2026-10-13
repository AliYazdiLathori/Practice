# LeetCode 63. Unique Paths II
# Difficulty: Medium
#
# Problem: A robot starts at the top-left of an m x n grid and wants to
# reach the bottom-right, moving only right or down. Some cells contain
# obstacles (1) that the robot cannot step on (0 = free cell). Return the
# number of unique paths to the bottom-right corner.
#
# Approach: Dynamic programming (top-down / memoization). The number of
# ways to reach cell (x, y) is the ways to reach the cell above plus the
# ways to reach the cell to the left. Obstacle cells are pre-filled with
# 0 ways, so no path can pass through them. Recursion starts at the
# destination and caches every computed cell so each is solved only once.
#
# Time complexity: O(m * n) - each cell is computed once, then reused
# Space complexity: O(m * n) - memo matrix, plus recursion stack
#                    up to O(m + n) deep

class Solution:

    def calculate(self, x, y, obstacleGrid, matrix):

        # Out of bounds: no paths come from outside the grid
        if x < 0 or y < 0:
            return 0

        # Already computed (-1 means "not yet visited", since 0 is a
        # valid result) - return the cached value
        if matrix[x][y] != -1:
            return matrix[x][y]

        # Top row, or obstacle directly above: can only arrive from the left
        elif x == 0 or obstacleGrid[x-1][y] == 1:
            matrix[x][y] = self.calculate(x, y-1, obstacleGrid, matrix)
            return matrix[x][y]
        # Left column, or obstacle directly to the left: can only arrive from above
        elif y == 0 or obstacleGrid[x][y-1] == 1:
            matrix[x][y] = self.calculate(x-1, y, obstacleGrid, matrix)
            return matrix[x][y]

        # Interior cell: paths from above + paths from the left
        matrix[x][y] = self.calculate(x-1, y, obstacleGrid, matrix) + self.calculate(x, y-1, obstacleGrid, matrix)
        return matrix[x][y]


    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        m = len(obstacleGrid)     # number of rows
        n = len(obstacleGrid[0])  # number of columns

        # -1 = "not computed yet"
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        matrix[0][0] = 1  # base case: one way to be at the start

        # Obstacle cells have 0 ways to be reached.
        # (This also zeroes the start cell if it is blocked.)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0

        # Destination is blocked: no path possible
        if obstacleGrid[-1][-1] == 1:
            return 0

        return self.calculate(m-1, n-1, obstacleGrid, matrix)



if __name__ == "__main__":

    solution = Solution()
    print(solution.uniquePathsWithObstacles([[1, 0]]))