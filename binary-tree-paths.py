# coding: utf-8

class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        self.ret = []
        self._binaryTreePaths(root, '')
        return self.ret

    def _binaryTreePaths(self, root, path):
        if root:
            path += str(root.val) if not path else ('->' + str(root.val))
            # print path
            if root.left:
                self._binaryTreePaths(root.left, path)
            if root.right:
                self._binaryTreePaths(root.right, path)
            if not (root.left or root.right):
                self.ret.append(path)

# easy: http://lintcode.com/zh-cn/problem/binary-tree-paths/
