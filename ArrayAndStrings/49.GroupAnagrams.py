## Group Anagrams (LeetCode 49)
"""
This solution groups words that are anagrams of each other using a dictionary.   # type: ignore
Each word is converted into a sorted character key, and words with the same key are grouped together.

Time Complexity: O(n * k log k)  
Space Complexity: O(n)
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # using Dictionary to solve this problem

        group = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in group:
                group[key] = []
            group[key].append(word)

        return list(group.values()) 

if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))   
