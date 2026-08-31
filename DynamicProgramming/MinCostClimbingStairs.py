from typing import List


class Solution:
    """
    LeetCode 746: Min Cost Climbing Stairs

    Problem: Given an array `cost` where cost[i] is the cost of stepping on
    stair i, find the minimum cost to reach the top of the staircase. You can
    start from step 0 or step 1, and from any step you can climb 1 or 2 steps.

    Approach: Bottom-up dynamic programming. `costs[i]` holds the minimum
    cost to REACH step i (not the cost of standing on it). Since you can
    only arrive at step i from step i-1 or step i-2, the cheapest way to
    reach i is whichever of those two predecessor paths (plus the cost of
    stepping off that predecessor) is smaller. A sentinel 0 is appended to
    `cost` to represent stepping "past" the last stair (the actual top),
    so costs[-1] ends up being the answer.

    Time complexity: O(n) - single pass over the stairs.
    Space complexity: O(n) - the `costs` DP array.
    """

    def calculator(self, costs, cost, step):
        # Cost to reach `step` = min of (cost to reach step-1 + price to
        # leave step-1) and (cost to reach step-2 + price to leave step-2).
        return min(costs[step-1]+cost[step-1], costs[step-2]+cost[step-2])
        

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Sentinel step representing "the top" — landing here is free,
        # it just lets us reuse the same recurrence for the final answer.
        cost.append(0)

        # costs[i] = minimum cost to REACH step i (base cases costs[0] and
        # costs[1] are correctly left at 0, since you can start free at
        # either step 0 or step 1).
        costs = [0] * (len(cost))

        for i in range(2, len(cost)):
            costs[i] = self.calculator(costs, cost, i)
            #print("step : ", i, "result : ", costs[i])

        # costs[-1] is the min cost to reach the sentinel "top" step,
        # i.e. the answer to the problem.
        return(costs[-1])


if __name__ == "__main__":
    solution = Solution()
    result = solution.minCostClimbingStairs([10,15,20])