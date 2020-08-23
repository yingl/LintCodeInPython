"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the linked list to be simplify.
    @return: return the linked list after simplifiction.
    """
    def simplify(self, head):
        # write your code here
        if not head:
            return head
        tail = head
        size = 1
        while tail.next:
            size += 1
            tail = tail.next
        if size <= 2:
            size = ''
        else:
            size = str(size - 2)
        new_tail = head
        for c in size:
            node = ListNode(str(ord(c)))
            new_tail.next = node
            new_tail = node
        if tail != head:
            new_tail.next = tail
        return head
        
# easy: https://www.lintcode.com/problem/linked-list-simplification/
