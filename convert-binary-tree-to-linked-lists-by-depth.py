"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
        ret = []
        curr_stack = [root]
        next_stack = []
        while curr_stack:
            head, tail = None, None
            for node in curr_stack:
                list_node = ListNode(node.val)
                if not head:
                    head = list_node
                    tail = head
                else:
                    tail.next = list_node
                    tail = tail.next
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            ret.append(head)
            curr_stack, next_stack = next_stack, []
        return ret

# easy: https://www.lintcode.com/problem/convert-binary-tree-to-linked-lists-by-depth/
