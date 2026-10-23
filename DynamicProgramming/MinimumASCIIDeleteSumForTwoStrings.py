class Solution:
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]

        def calculate(s1, s2, i, j, dp) -> int:
            if i > len(s1)-1:
                cost = 0
                for k in range(j, len(s2)):
                    cost += ord(s2[k])
                return cost
            
            if j > len(s2)-1:
                cost = 0
                for k in range(i, len(s1)):
                    cost += ord(s1[k])
                return cost

            
            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                if s1[i:] == s2[j:]:
                    return 0
                
                dp[i][j] = 0 + calculate(s1,s2, i+1 ,j+1,dp)

            else:
                dp[i][j] = min(calculate(s1,s2, i+1 ,j+1,dp)+ord(s1[i])+ord(s2[j]), calculate(s1,s2, i ,j+1,dp)+ ord(s2[j]), calculate(s1,s2, i+1 ,j,dp)+ord(s1[i]))

            return dp[i][j]

        return calculate(s1,s2, 0,0, dp)
        


if __name__  == "__main__":
    solution = Solution()
    print(solution.minimumDeleteSum("delete", "leet"))