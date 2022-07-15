# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        Map = {}
        
        def traverse(curr):
            while(curr):
                if Map.get(curr):
                    return curr
                
                Map[curr] = True
                curr = curr.next
                
        traverse(headA)
        
        return traverse(headB)
        
       
        
        
        