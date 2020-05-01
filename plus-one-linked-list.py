"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        new_head = self.reverse(head)
        flag = 1
        node = new_head
        prev = None
        while node:
            node.val += flag
            flag = int(node.val / 10)
            node.val %= 10
            prev = node
            node = node.next
        if flag > 0:
            prev.next = ListNode(flag)
        return self.reverse(new_head)
        
    def reverse(self, head):
        new_head = None
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        return new_head
        
# medium: https://www.lintcode.com/problem/plus-one-linked-list/
