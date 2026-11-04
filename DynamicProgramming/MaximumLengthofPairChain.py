class Solution:
    def calculate(self,dp, parirs, i):
        length = 1
        
        if dp[i] != 0:
            return dp[i]

        for j in range(len(parirs)):
            if i == j:
                continue

            if parirs[i][0] > parirs[j][1]:
                if length < self.calculate(dp, parirs, j)+1:    
                    length = self.calculate(dp, parirs, j)+1

        dp[i] = length
        return dp[i]
            
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        
        dp = [0] * len(pairs)

        for i in range(len(pairs)):
            self.calculate(dp,pairs,i)

        return max(dp)



if __name__ == "__main__":
    solution = Solution()
    print(solution.findLongestChain([[1,2],[7,8],[4,5]]))