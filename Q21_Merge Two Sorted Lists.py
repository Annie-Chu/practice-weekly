class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_node = ListNode(0)
        prev = new_node
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        if l1 == None:
            prev.next = l2

        if l2 == None:
            prev.next = l1

        return new_node.next
