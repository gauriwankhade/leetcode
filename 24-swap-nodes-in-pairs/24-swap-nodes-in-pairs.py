# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head:
            return
        curr = head
        newhead = head.next
        last = None
        
        while(curr and curr.next):
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            
            if last:
                last.next = temp
                
            last = curr
            curr = curr.next
           
        return newhead or head
            