# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        curr = head
        newHead = None
        last = None
        
        while(curr and curr.next):
            print(curr.val, curr.next.val)
            if not newHead:
                newHead = curr.next
            
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            
            if last:
                last.next = temp
                
            last = curr
            curr = curr.next
           
        return newHead or head
            