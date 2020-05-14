class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
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

    if l1 is None:
        prev.next = l2

    if l2 is None:
        prev.next = l1

    return new_node.next


def lst2link(list):
    cur = cur2 = ListNode(0)
    for i in list:
        cur.next = ListNode(i)
        cur = cur.next

    return cur2.next


def display(l3):
    l4 = []
    cur_node = l3

    while cur_node is not None:

        l4.append(cur_node.val)
        cur_node = cur_node.next

    return l4


if __name__ == '__main__':

    a = lst2link([1, 2, 4])
    b = lst2link([1, 3, 4])

    res = mergeTwoLists(a, b)
    final = display(res)

    print(final)




