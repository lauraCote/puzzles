# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
       
    
    def merge(self, l1: ListNode, l2: ListNode, result: ListNode) -> ListNode:
        if l1 == None && l2 == None:
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
        merge(l1, l2, result)

