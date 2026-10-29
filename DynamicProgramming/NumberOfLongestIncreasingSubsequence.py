class Solution:



        

    def findNumberOfLIS(self, nums: list[int]) -> int:

        dp = [1] * len(nums)
        track = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])

            if dp[i] > 1:
                track[i] = 0
            for j in range(i):
                if dp[i] - 1 == dp[j] and nums[i] > nums[j]:
                    track[i] += track[j]


        maximum = max(dp)
        passes = 0
        #print(dp, maximum)
        for i in range(len(nums)):
            if dp[i] == maximum:
                passes += track[i]


        return passes




if __name__ == "__main__":
    solution = Solution()
    print(solution.findNumberOfLIS([6,4,7]))
    print(solution.findNumberOfLIS([1,2,4,3,5,4,7,2]))
    print(solution.findNumberOfLIS([2,2,2,2,2]))
    print(solution.findNumberOfLIS([1,3,5,4,7]))
    
