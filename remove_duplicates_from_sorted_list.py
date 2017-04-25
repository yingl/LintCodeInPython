# coding: utf-8

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        node = head
        while node is not None:
            val = node.val
            next_node = node.next
            while next_node:
                if next_node.val == val:
                    next_node = next_node.next
                else:
                    break
            if next_node != node.next:
                node.next = next_node
            node = node.next
        return head

# easy: http://lintcode.com/zh-cn/problem/remove-duplicates-from-sorted-list/
