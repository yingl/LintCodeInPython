# coding: utf-8

class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        # write your code here
        if node.next is None:
            node = None
        else:
            p = node.next
            node.val = p.val
            node.next = p.next

# easy: http://lintcode.com/problem/delete-node-in-the-middle-of-singly-linked-list
