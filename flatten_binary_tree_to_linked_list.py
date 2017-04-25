# coding: utf-8

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if not root:
            return None
        head, tail = self.dfs(root)
        return head

    def dfs(self, root):
        if not (root.left or root.right):
            return root, root
        head, tail = root, root
        left_head, left_tail = None, None
        right_head, right_tail = None, None
        if root.left:
            left_head, left_tail = self.dfs(root.left)  # 将左子树拆成链表
        if root.right:
            right_head, right_tail = self.dfs(root.right) # 将右子树拆成链表
        if left_head: # 插入左子树拆成的链表
            root.right = left_head
            left_tail.right = right_head
            tail = right_tail if right_tail else left_tail
        else: # 没有左子树
            tail = right_tail
        head.left = None
        return head, tail

# easy: http://lintcode.com/zh-cn/problem/flatten-binary-tree-to-linked-list/
