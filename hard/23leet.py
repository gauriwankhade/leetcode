# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        listMap = {}
        self.traverseList(lists, listMap)

        sortedMap = sorted(listMap)

        head = prev = None
        for key in sortedMap:
            for counter in range(listMap[key]):
                n = ListNode(key)
                if prev:
                    prev.next = n
                    prev = n
                else:
                    head = prev = n


        return head
        


    def traverseList(self, lists, listMap):
        for item in lists:
            curr = item
            while(curr):
                key = listMap.get(curr.val)
                if key:
                    listMap[curr.val] += 1
                else:
                    listMap[curr.val] = 1
                curr = curr.next


    def printList(self, head):
        while(head):
            print(head.val)
            head = head.next

        

s = Solution()
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)


s.printList(s.mergeKLists([]))






