from typing import List


class Solution:
    def calculator(self, costs, cost, step):
        return min(costs[step-1]+cost[step-1], costs[step-2]+cost[step-2])
        

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        costs = [0] * (len(cost))
        for i in range(2, len(cost)):
            costs[i] = self.calculator(costs, cost, i)
            #print("step : ", i, "result : ", costs[i])

        return(costs[-1])


if __name__ == "__main__":
    solution = Solution()
    result = solution.minCostClimbingStairs([10,15,20])