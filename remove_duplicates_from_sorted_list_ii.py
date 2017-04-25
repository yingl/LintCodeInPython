# coding: utf-8

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        new_head, new_tail = None, None
        old_node = head
        while old_node:
            next_node = old_node.next
            if (next_node is None) or (next_node.val != old_node.val):
                if new_head is None:
                    new_head = old_node
                else:
                    new_tail.next = old_node
                new_tail = old_node
                new_tail.next = None
                old_node = next_node
            else:
                # 跳过重复的节点
                while next_node and (next_node.val == old_node.val):
                    next_node = next_node.next
                old_node = next_node
        return new_head

# medium: http://lintcode.com/zh-cn/problem/remove-duplicates-from-sorted-list-ii/
