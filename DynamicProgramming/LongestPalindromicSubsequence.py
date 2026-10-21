from typing import List

class Solution:

    def calculate(self, i , j , s, memo) -> int:
        if i == j:
            return 1
        elif j < i:
            return 0
        if s[i] == s[j]:
            if memo[i][j] == 0:
                memo[i][j] = max(2 + self.calculate(i+1, j-1, s, memo), 0 + self.calculate(i+1, j, s, memo), 0 + self.calculate(i, j-1, s, memo))
            return memo[i][j]
        if s[i] != s[j]:
            if memo[i][j] == 0:
                memo[i][j] = 0 + max(self.calculate(i, j-1, s, memo),self.calculate(i+1, j , s, memo))
            return memo[i][j]

        
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = memo = [[0 for _ in range(len(s))] for _ in range(len(s))]
        return self.calculate(0, len(s)-1, s, memo)

        

        


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindromeSubseq("bbbab"))