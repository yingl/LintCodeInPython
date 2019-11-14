# coding: utf-8

class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        return self._buildTree(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def _buildTree(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if in_start >= in_end:
            return None
        i = in_start
        while i < in_end:
            if inorder[i] == preorder[pre_start]:   # 找到根节点
                break
            i += 1
        root = TreeNode(inorder[i])
        left_len = i - in_start # 左子树元素数量
        # 生成左子树
        root.left = self._buildTree(preorder, pre_start + 1, pre_start +1 + left_len, inorder, in_start, i)
        # 生成右子树
        root.right = self._buildTree(preorder, pre_start + 1 + left_len, pre_end, inorder, i + 1, in_end)
        return root

# medium: http://lintcode.com/zh-cn/problem/construct-binary-tree-from-preorder-and-inorder-traversal/
