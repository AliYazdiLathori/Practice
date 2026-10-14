# LeetCode 120. Triangle
# Difficulty: Medium
#
# Problem: Given a triangle array, return the minimum path sum from top
# to bottom. At each step you may move to an adjacent number on the row
# below: from index i, you can go to index i or i+1 on the next row.
#
# Approach: Dynamic programming (top-down accumulation, done in place).
# Walk down the triangle one row at a time and update each element of the
# next row with the cheapest cost to reach it. The leftmost element can
# only come from the leftmost element above, the rightmost can only come
# from the rightmost above, and every middle element comes from the
# cheaper of its two parents above. After the last row is updated, each
# element holds the minimum path sum ending there, so the answer is the
# minimum of the last row.
#
# Time complexity: O(N) - where N is the total number of elements in the
#                  triangle (each element is updated once)
# Space complexity: O(R) - where R is the number of rows; the only extra
#                  space is the recursion stack (input is modified in place)

class Solution:

    def calculate(self, height, triangle):

        # Base case: we've reached the last row, so every element already
        # holds its minimum path sum. The answer is the smallest of them.
        if height == len(triangle) - 1:
            return min(triangle[height])

        # Update each element of the next row with its cheapest path cost
        for i in range(len(triangle[height+1])):
            # Leftmost element: only one parent (directly above-left edge)
            if i == 0:
                triangle[height+1][i] = triangle[height+1][i] + triangle[height][i]

            # Rightmost element: only one parent (the last element above)
            elif i == len(triangle[height+1]) - 1:
                triangle[height+1][i] = triangle[height+1][i] + triangle[height][i-1]

            # Middle element: add the cheaper of its two parents above
            else:
                triangle[height+1][i] = triangle[height+1][i] + min(triangle[height][i-1], triangle[height][i])

        # Move down to the next row
        return self.calculate(height+1, triangle)






    def minimumTotal(self, triangle: list[list[int]]) -> int:

        costMatrix = [0 for _ in range(len(triangle))]
        costMatrix[0] = triangle[0][0]

        # Start from the top row (height 0)
        return self.calculate(0, triangle)








if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))