# coding: utf-8

class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(0, head)
        tmp_head, tmp_tail = dummy, dummy
        for i in xrange(n): # 1 <= m <= n <= 链表长度
            if i < m:
                prev = tmp_head
                tmp_head = tmp_head.next
            tmp_tail = tmp_tail.next
        _next = tmp_tail.next
        tmp_head.next = None
        tmp_head = self.reverse(tmp_head)
        prev.next = tmp_head
        while tmp_head.next:
            tmp_head = tmp_head.next
        tmp_head.next = _next
        return dummy.next

    def reverse(self, head):
        if not head:
            return None
        new_head = None
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        return new_head

# medium: http://lintcode.com/zh-cn/problem/reverse-linked-list-ii/
