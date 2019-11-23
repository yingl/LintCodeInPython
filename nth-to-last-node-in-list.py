# coding: utf-8

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        before_node = head
        after_node = head
        for i in xrange(0, n):
            before_node = before_node.next
        while before_node is not None:
            before_node = before_node.next
            after_node = after_node.next
        return after_node

# easy: http://lintcode.com/zh-cn/problem/nth-to-last-node-in-list/
