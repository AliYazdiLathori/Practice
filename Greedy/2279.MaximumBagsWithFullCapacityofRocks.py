from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        differentialList = []
        for i in range(len(capacity)):
            differentialList.append(capacity[i]-rocks[i])
        
        differentialList.sort()
        fullBags = 0
        requireStones = 0
        for i in range(len(differentialList)):
            requireStones += differentialList[i]
            if requireStones <= additionalRocks:
                fullBags += 1
            else:
                break

        return fullBags
            
if __name__ == "__main__":
    capacity = [2,3,4,5]
    rocks = [1,2,4,4]
    additionalRocks = 2
    sol = Solution()
    print(sol.maximumBags(capacity, rocks, additionalRocks))