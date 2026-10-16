# LeetCode 931. Minimum Falling Path Sum
# Difficulty: Medium
#
# Problem: Given an n x n matrix of integers, return the minimum sum of
# any falling path. A falling path starts at any element in the first row
# and moves to the row below, going to the same column or to a column
# one position to the left or right (diagonally).
#
# Approach: Dynamic programming (bottom-up accumulation, done in place).
# Start from the second-to-last row and move upward. For each cell, add
# the smallest value among the (up to) three cells directly below it:
# below-left, below, and below-right. After processing a row, each cell
# holds the minimum falling-path sum starting from that cell down to the
# bottom. When we reach the top, the answer is the minimum of the first row.
#
# Time complexity: O(n^2) - every cell is updated exactly once
# Space complexity: O(n) - only the recursion stack (n rows deep);
#                  the input matrix is modified in place

class Solution:

    def calculate(self, matrix, depth):

        # Base case: we've processed every row above the last one, so the
        # first row now holds the min path sums. Return the smallest.
        if depth == -1:
            return min(matrix[0])

        for i in range(len(matrix[0])):

            # Left edge: no below-left neighbor, choose between below and below-right
            if i == 0:
                matrix[depth][i] += min(matrix[depth+1][i], matrix[depth+1][i+1])
                continue

            # Right edge: no below-right neighbor, choose between below and below-left
            elif i == len(matrix[0])-1:
                matrix[depth][i] += min(matrix[depth+1][i], matrix[depth+1][i-1])
                continue

            # Middle cell: choose the cheapest of the three cells below
            matrix[depth][i] += min(matrix[depth+1][i], matrix[depth+1][i-1], matrix[depth+1][i+1])

        # Move up to the previous row
        return self.calculate(matrix, depth-1)



    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        # Start at the second-to-last row (the last row's values are already
        # their own minimum path sums)
        return self.calculate(matrix, len(matrix)-2)



if __name__ == "__main__":

    solution = Solution()
    print(solution.minFallingPathSum([[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]))