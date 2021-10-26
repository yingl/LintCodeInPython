"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        if not head:
            return ListNode(val)
        if val <= head.val:
            return ListNode(val, head)
        curr, _next = head, head.next
        while curr and _next:
            if (curr.val <= val) and (_next.val >= val):
                t = ListNode(val, _next)
                curr.next = t
                return head
            curr = curr.next
            _next = _next.next
        curr.next = ListNode(val)
        return head

# easy: https://www.lintcode.com/problem/219/
