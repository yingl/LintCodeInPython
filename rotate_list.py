# coding: utf-8

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if not head:
            return head
        list_len = 0
        tail = None
        node = head
        while node: # 找到链表的尾部节点并统计链表长度
            list_len += 1
            tail = node
            node = node.next
        shift = k % list_len
        if shift == 0:
            return head
        new_tail = head
        for i in xrange(list_len - shift-1):
            new_tail = new_tail.next
        new_head = new_tail.next  # 找到新的head
        tail.next = head  # tail指向原来的head
        new_tail.next = None
        return new_head

# medium: http://lintcode.com/zh-cn/problem/rotate-list/
