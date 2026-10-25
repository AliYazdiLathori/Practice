# LeetCode 115. Distinct Subsequences
# Difficulty: Hard
#
# Problem: Given two strings s and t, return the number of distinct
# subsequences of s that equal t.
#
# Approach: Dynamic programming (top-down / memoization). Let dp[j][i] be
# the number of ways the first (j+1) characters of t can be formed as a
# subsequence of the first (i+1) characters of s. Work backwards from the
# ends of both strings:
#   - If s[i] != t[j]: s[i] can't help, so we skip it -> dp[j][i-1].
#   - If s[i] == t[j]: we can either skip s[i] (dp[j][i-1]) or use it to
#     match t[j] (dp[j-1][i-1]); the answer is the sum of both.
#   - Base case: when j == 0 and the characters match, using s[i] finishes
#     matching t, which counts as 1 extra way.
# Results are cached in dp so each (j, i) pair is solved only once.
#
# Time complexity: O(m * n) - where m = len(s), n = len(t); each state is computed once
# Space complexity: O(m * n) - dp table, plus recursion stack up to O(m) deep

class Solution:
    def calculate(self, s, t, i, j, dp) -> int:

        # No characters left in t or s to match against: no valid way
        if j < 0:
            return 0
        if i < 0:
            return 0

        # Already computed - return the cached value
        if dp[j][i] != -1:
            return dp[j][i]

        if s[i] == t[j]:
            if j == 0:
                # Matching the first char of t: skip s[i] + use s[i]
                # (+1 because using s[i] here completes the match of t's prefix)
                dp[j][i] = self.calculate(s, t, i-1, j, dp) + self.calculate(s, t, i-1, j-1, dp) + 1
            else:
                # Skip s[i], or use s[i] to match t[j] and match the rest of t earlier
                dp[j][i] = self.calculate(s, t, i-1, j, dp) + self.calculate(s, t, i-1, j-1, dp)

        else:
            # Characters differ: s[i] can't be used, so skip it
            dp[j][i] = self.calculate(s, t, i-1, j, dp)

        return dp[j][i]

    def numDistinct(self, s: str, t: str) -> int:

        # dp[j][i] = ways to form t[0..j] from s[0..i]; -1 means "not computed yet"
        dp = [[-1 for _ in range(len(s))] for _ in range(len(t))]

        # Start from the ends of both strings and work backwards
        return self.calculate(s, t, len(s)-1, len(t)-1, dp)






if __name__ == "__main__":
    solution = Solution()
    print(solution.numDistinct("babgbag", "bag"))