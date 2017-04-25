# coding: utf-8

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if not head:
            return None
        new_head = None
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        return new_head

# easy: http://lintcode.com/zh-cn/problem/reverse-linked-list/
