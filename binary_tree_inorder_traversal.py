# coding: utf-8

class Solution:
    def __init__(self):
        self.ret = []

    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if root is not None:
            self.inorderTraversal(root.left)    # 遍历左子树
            self.ret.append(root.val)
            self.inorderTraversal(root.right)   # 遍历右子树
        return self.ret

    def loopVersion(self, root):    # 非递归版本
        ret, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                ret.append(root.val)
                root = root.right
        return ret

# easy: http://lintcode.com/zh-cn/problem/binary-tree-inorder-traversal/
