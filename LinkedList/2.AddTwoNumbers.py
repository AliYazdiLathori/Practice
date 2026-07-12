"""
Idea:
Simulate elementary-school addition by first extracting the digits from both
linked lists, then add corresponding digits while carrying over any overflow.
Finally, build the resulting linked list from the computed digits.

Approach:
- Traverse both linked lists and store their digits in arrays.
- Iterate through both arrays up to the longer length.
- Add corresponding digits along with the carry.
- Append the final carry if it exists.
- Construct the answer as a new linked list from the resulting digits.

Topics:
Linked List, Simulation, Math

Time Complexity:
O(n + m)
  # Traverse both lists once, perform one addition pass, and build the result.

Space Complexity:
O(n + m)
  # Extra arrays store the digits before constructing the output list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sumfunction(self, first, second, helper):
        sum = first+ second+ helper
        return sum%10 , int(sum/10)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digitsl1 = []
        digitsl2 = []
        while l1:
            digitsl1.append(l1.val)
            l1 = l1.next
        while l2:
            digitsl2.append(l2.val)
            l2 = l2.next

        results = []
        helper = 0
        for i in range(max(len(digitsl1), len(digitsl2))):
            if i < len(digitsl1) and i < len(digitsl2):
                result, helper = self.sumfunction(digitsl1[i], digitsl2[i], helper)
                
            elif i < len(digitsl1):
                result, helper = self.sumfunction( digitsl1[i], 0,helper)

            else:
                result, helper = self.sumfunction( 0, digitsl2[i],helper)

            results.append(result)
        
        if helper>0:
            results.append(helper)
        
        dummy = ListNode()
        current = dummy

        for x in results:
            current.next = ListNode(x)
            current = current.next

        return dummy.next
        