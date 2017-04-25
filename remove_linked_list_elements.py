# coding: utf-8

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        prev, node = None, head
        while node:
            if node.val == val:
                if not prev:
                    head = node.next
                else:
                    prev.next = node.next
            else:
                prev = node
            node = node.next
        return head
        
# entry: http://www.lintcode.com/zh-cn/problem/remove-linked-list-elements/
