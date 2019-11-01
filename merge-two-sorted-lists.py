# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
       result = ListNode(0)
       self.merge(l1, l2, result)
       return result.next
    
    def merge(self, l1: ListNode, l2: ListNode, result: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return result
        elif l1 == None:
            result.next = l2
            return result
        elif l2 == None:
            result.next = l1
            return result
        if l1.val < l2.val:
            result.next = l1
            l1 = l1.next
        else:
            result.next = l2
            l2 = l2.next

        result = result.next
        self.merge(l1, l2, result)


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(7)

l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(6)

result = Solution().mergeTwoLists(l1, l2)

while result != None:
    print(result.val)
    result = result.next