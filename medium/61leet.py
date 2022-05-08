#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        length = self.listLength(head)
        k = k%length
        # print('k-', k, 'length-', length)
        counter = 0
        prev = curr = head
        newHead =  newTail = None

        if k<1:
            return head
        while(curr):
            if length - counter == k  :
                newHead = curr
                newTail = prev
           
            prev = curr
            counter += 1
            if curr:
                curr = curr.next
       
        prev.next = head
        head = newHead
        newTail.next = None


        return head


    def listLength(self, head):
        len = 0
        while(head):
            len += 1
            head = head.next
        return len

    def printList(self, head):
        while(head):
            print(head.val)
            head = head.next


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

s.printList(s.rotateRight(head, 2000000000))


       