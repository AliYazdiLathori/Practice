# LeetCode 70. Climbing Stairs
# Difficulty: Easy
#
# Problem: You are climbing a staircase with n steps. Each move you can
# climb either 1 or 2 steps. Count the distinct number of ways to reach
# the top.
#
# Approach: Dynamic programming (bottom-up). The number of ways to reach
# step i is the sum of the ways to reach step i-1 (then take a 1-step)
# and step i-2 (then take a 2-step) — this is just the Fibonacci
# sequence in disguise. ways[i] = ways[i-1] + ways[i-2].
#
# Time complexity: O(n) - single pass filling the ways array
# Space complexity: O(n) - array of size n+1 to store all intermediate results
#                    (could be optimized to O(1) with two variables)

class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n+1)
        ways[0] = 1  # 1 way to "climb" 0 stairs (do nothing)
        ways[1] = 1  # 1 way to climb 1 stair (a single 1-step)
        for i in range(2, n+1):
            # ways to reach step i = ways to reach (i-2) + ways to reach (i-1)
            ways[i] = ways[i-2] + ways[i-1]

        return ways[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(3))