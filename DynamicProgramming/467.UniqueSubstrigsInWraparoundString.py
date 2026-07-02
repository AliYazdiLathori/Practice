
"""
Problem: Unique Substrings in Wraparound String
Platform: LeetCode
Difficulty: Medium

Approach:
This solution scans the string while maintaining the length of the current valid wraparound streak.

A dictionary (`longestStrike`) stores, for each lowercase letter, the maximum length of a valid wraparound substring ending with that letter. Whenever a streak ends, the algorithm traverses the streak backward and updates these maximum lengths. Only larger values are kept, since shorter streaks ending with the same character cannot produce additional unique substrings.

After processing all streaks (including the final one), the answer is obtained by summing the maximum lengths stored for all 26 letters.

Time Complexity: O(n)
Space Complexity: O(1)
https://leetcode.com/problems/unique-substrings-in-wraparound-string/?envType=problem-list-v2&envId=dv7mwfpv
"""

class Solution:
    def countMaxSubstring(self, substring, longestStrike, i , s):
        counter = 1
        while substring > 0:
            longestStrike[s[i-counter]] = max(substring,longestStrike[s[i-counter]])
            substring -= 1
            counter += 1
        return longestStrike

    def findSubstringInWraproundString(self, s: str) -> int:
        longestStrike = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
            'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
            'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
            's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
            'y': 0, 'z': 0
        }
        substring = 1
        for i in range(1, len(s)):
            
            if (ord(s[i]) - ord(s[i-1])) == 1 or (ord(s[i]) == 97 and ord(s[i-1]) == 122):
                substring += 1
            else:
                longestStrike = self.countMaxSubstring(substring, longestStrike, i ,s)
                substring = 1
        
        self.countMaxSubstring(substring, longestStrike, len(s), s)
        result = sum(longestStrike.values())
        return result
                
                
if __name__ == "__main__":
    s = Solution()
    print(s.findSubstringInWraproundString("zab"))  # Output: 6
    print(s.findSubstringInWraproundString("cac"))  # Output: 2
    print(s.findSubstringInWraproundString("a"))    # Output: 1
