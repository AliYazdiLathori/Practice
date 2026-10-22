"""LeetCode 72: Edit Distance.

Find the minimum number of insertions, deletions, or substitutions needed to
turn one word into another. The solution uses recursive dynamic programming
with memoization over pairs of character indices.

Difficulty: Hard.
Time: O(mn), where m and n are the word lengths; each index pair is computed
once. Space: O(mn) for the memo table, plus O(m+n) for the recursion stack.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def calculate(word1, word2, i , j, dp):
            # If either word is exhausted, the remaining characters must be inserted or deleted.
            if i > len(word1)-1:
                return len(word2) - j

            if j > len(word2)-1:
                return len(word1) - i
            
            # Reuse the result for this pair of character indices.
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = 0 + calculate(word1, word2, i+1, j+1, dp)

            else:
                # Try substitution, insertion, and deletion; choose the cheapest.
                dp[i][j] = 1 + min(calculate(word1, word2, i+1 , j+1 ,dp), calculate(word1, word2, i , j+1 ,dp), calculate(word1, word2, i+1 , j ,dp))    

            return dp[i][j]
        


        dp = [[-1 for j in range(len(word2))]for i in range(len(word1))]

        return(calculate(word1,word2,0,0, dp))

        



if __name__ == "__main__":
    solution = Solution()
    print(solution.minDistance( "horse", "ros"))