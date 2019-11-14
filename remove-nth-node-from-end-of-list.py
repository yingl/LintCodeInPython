# coding: utf-8

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        '''
        第一个node向向前走n步，然后两个node一起走。
        走的时候记住记住后面一个node的prev节点.
        '''
        first, second = head, head
        for i in xrange(0, n):
            first = first.next
        prev = None
        while first:
            first = first.next
            prev = second
            second = second.next
        if not prev:  # 删除head节点
            return head.next
        else:
            prev.next = second.next
            return head

# easy: http://lintcode.com/problem/remove-nth-node-from-end-of-list
