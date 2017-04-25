# coding: utf-8

class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        if not head:
            return None
        new_head = ListNode(0)
        while head:
            tmp = new_head
            next = head.next
            while tmp.next and tmp.next.val < head.val:
                tmp = tmp.next
            head.next = tmp.next
            tmp.next = head
            head = next
        return new_head.next

# easy: http://lintcode.com/zh-cn/problem/insertion-sort-list/
