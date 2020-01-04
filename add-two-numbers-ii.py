"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # write your code here
        head, tail = None, None
        step = 0
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        while l1 and l2:
            val = l1.val + l2.val + step
            step = int(val / 10)
            val = val % 10
            if not head:
                head = tail = ListNode(val)
            else:
                tail.next = ListNode(val)
                tail = tail.next
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            l = l1 if l1 else l2
            while l:
                val = l.val + step
                step = int(val / 10)
                val = val % 10
                if not head:
                    head = tail = ListNode(val)
                else:
                    tail.next = ListNode(val)
                    tail = tail.next
                l = l.next
        if step:
            tail.next = ListNode(step)
            tail = tail.next
        return self.reverse(head)
    
    def reverse(self, node):
        head, tail = None, None
        while node:
            if not head:
                head, tail = node, node
                node = node.next
                tail.next = None
            else:
                tmp = node.next
                node.next = head
                head = node
                node = tmp
        return head

# medium: https://www.lintcode.com/problem/add-two-numbers-ii/
