# coding: utf-8

class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        small_head, small_tail = None, None
        big_head, big_tail = None, None
        while head is not None:
            next = head.next
            head.next = None
            if head.val < x:
                if small_head is None:
                    small_head = head
                else:
                    small_tail.next = head
                small_tail = head
            else:
                if big_head is None:
                    big_head = head
                else:
                    big_tail.next = head
                big_tail = head
            head = next
        if small_tail is not None:
            small_tail.next = big_head
        return small_head if small_head else big_head

# easy: http://lintcode.com/zh-cn/problem/partition-list/
