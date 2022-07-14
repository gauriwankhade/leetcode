# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        curr = head
        last = None
        
        while(curr):
            nextCurr = curr.next
            if not last:
                last = curr
                curr.next = None
            else:  
                curr.next = last
                last = curr
           
            curr = nextCurr
            
            
        return last
                
        