class Solution:
    def longestPalindrome(self, s: str) -> str:

        maximum = ""

        for i in range(len(s)):
            for j in range(i, len(s)):

                substring = s[i:j+1]

                if substring == substring[::-1]:
                    
                    if len(maximum) < len(substring):
                        maximum = substring

        return maximum




        



if __name__ == "__main__":

    solution = Solution()
    print(solution.longestPalindrome("babad"))