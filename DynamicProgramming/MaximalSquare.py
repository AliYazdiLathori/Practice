# LeetCode 221. Maximal Square
# Difficulty: Medium
#
# Problem: Given an m x n binary matrix filled with "0"s and "1"s, find
# the largest square containing only "1"s and return its area.
#
# Approach: Dynamic programming (bottom-up, from bottom-right to top-left).
# squares[i][j] stores the side length of the largest all-"1" square whose
# TOP-LEFT corner is at (i, j). If the cell is "0", the value is 0.
# Otherwise it is 1 + the minimum of the three neighbors that would form
# the rest of the square: right (i, j+1), below (i+1, j), and diagonal
# (i+1, j+1). The minimum is used because the square can only grow as
# large as the smallest of those three squares allows. The last row and
# last column are base cases (a square there can only have side 0 or 1).
# The answer is the largest side length found, squared.
#
# Time complexity: O(m * n) - every cell is visited once
# Space complexity: O(m * n) - the squares DP table

class Solution:

    def maximalSquare(self, matrix: list[list[str]]) -> int:

        # DP table: squares[i][j] = side of the largest square with top-left at (i, j)
        squares = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        # Base case: last column (a square here can be at most 1x1)
        for i in range(len(matrix)):
            squares[i][-1] = int(matrix[i][-1])

        # Base case: last row (a square here can be at most 1x1)
        for j in range(len(matrix[0])):
            squares[-1][j] = int(matrix[-1][j])

        # Fill the rest of the table from bottom-right up to top-left
        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[0])-2, -1, -1):

                # A "0" cell cannot be part of any square
                if matrix[i][j] == "0":
                    squares[i][j] = 0
                    continue

                # Extend the smallest of the right, below, and diagonal squares by 1
                squares[i][j] = 1 + min(squares[i+1][j], squares[i][j+1], squares[i+1][j+1])

        # Largest side length anywhere in the table; area = side * side
        maximum = max(max(row) for row in squares)
        return maximum * maximum




if __name__ == "__main__":

    solution = Solution()
    print(solution.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))