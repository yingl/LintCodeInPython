# coding: utf-8

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        dummy_node = ListNode(0)  # 这个很重要，不然head处理非常麻烦！
        dummy_node.next = head
        prev, node = dummy_node, dummy_node.next
        while node:
            _next = node.next
            if not _next:
                break # 结束
            # 交换参考swap_two_nodes_in_linked_list.py
            prev.next = _next
            tmp = _next.next
            _next.next = node
            node.next = tmp
            prev = node
            node = node.next
        return dummy_node.next

# easy: http://lintcode.com/zh-cn/problem/swap-nodes-in-pairs/
