"""LeetCode 139: Word Break

Problem: Determine whether the string can be segmented into one or more
dictionary words.
Approach: Recursively try dictionary-word suffixes and check whether the
remaining prefix can also be segmented. Memoize each prefix result to avoid
repeating work.

Difficulty: Medium
Time complexity: O(n^3) in Python, accounting for substring creation and hashing.
Space complexity: O(n^2) for memoized prefix strings, plus O(n) recursion depth.
"""


class Solution:
    def calculate(self, s: str, wordDict, memo) -> bool:

        # Reuse the result when this prefix has already been evaluated.
        if s in memo:
            return memo[s]

        # Try each suffix as the final dictionary word.
        for i in range (len(s)-1, -1,-1):


            if s[i:] in wordDict:
                
                # A dictionary word covering the whole prefix completes it.
                if i == 0:
                    return True

                # The prefix is breakable if its remaining left part is breakable.
                if self.calculate(s[:i],wordDict,memo):
                    memo[s] = True
                    return True

            # No split can succeed if even the full prefix was not a dictionary word.
            if i == 0:
                return False
        
        # Cache failure so this prefix is not explored again.
        memo[s] = False
        return False    
        
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = {}
        # Set membership makes checking candidate words efficient.
        words = set(wordDict)
        return(self.calculate(s,words, memo))
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.wordBreak("aaabaaa", wordDict = ["a"]))