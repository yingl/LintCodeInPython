# coding: utf-8

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        # Write your code here
        dummy_node = ListNode(0)
        dummy_node.next = head
        v1_prev, v1_node = self.findNode(dummy_node, v1)
        v2_prev, v2_node = self.findNode(dummy_node, v2)
        '''
        难点在下面，因为不能直接交换两个元素的值，
        要特别小心类似v1_node.next等于v2_node的情况。
        两种具体分析如下：
        1. p1->v1->v2->n2 => p1->v2->v1->n2
          - p1->v2 (tmp = n2)
          - p1->v2->v1
          - p1->v2->v1->n2(tmp)
        2. p2->v2->v1->n1 => p2->v1->v2->n1
          - p2->v2->v2 (tmp = v2)
          - p2->v2->n1
          - p2->v1
          - p2->v1->v2->n1
        对于普通情况
        1. p1->v1->n1->p2->v2->n2
          - p1->v2 (tmp = n2)
          - p1->v2->n1
          - p2->n1
          - p2->n1->n2
        2. p2->v2->n2->p1->v1->n2
          - 类似上面
        整个比较精妙的地方在于用dummy_node解决v1/v2可能是head的问题。
        '''
        if v1_node and v2_node:
            v1_prev.next = v2_node
            tmp = v2_node.next
            if v1_node.next == v2_node:
                v2_node.next = v1_node
                v1_node.next = tmp
            else:
                v2_node.next = v1_node.next
                v2_prev.next = v1_node
                v1_node.next = tmp
        return dummy_node.next

    def findNode(self, head, val):
        while head.next:
            if head.next.val == val:
                    return head, head.next
            head = head.next
        return None, None

# medium: http://lintcode.com/zh-cn/problem/swap-two-nodes-in-linked-list/
