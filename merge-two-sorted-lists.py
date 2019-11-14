# coding: utf-8

class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        head, tail = None, None
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            if not head:
                head = node
            else:
                tail.next = node
            tail = node
        node = l1 if l1 else l2
        if not head:
            head = node
        else:
            tail.next = node
        tail = node
        return head

# easy: http://lintcode.com/zh-cn/problem/merge-two-sorted-lists/
