# coding: utf-8

class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        return self._buildTree(inorder, 0, len(inorder), postorder, 0, len(postorder))

    def _buildTree(self, inorder, in_start, in_end, postorder, post_start, post_end):
        if in_start >= in_end:
            return None
        i = in_start
        while i < in_end:
            if inorder[i] == postorder[post_end -1]:    # 找到根节点
                break
            i += 1
        root = TreeNode(inorder[i])
        left_len = i - in_start # 左子树元素数量
        root.left = self._buildTree(inorder, in_start, i, postorder, post_start, post_start + left_len)
        root.right = self._buildTree(inorder, i + 1, in_end, postorder, post_start + left_len, post_end - 1)
        return root

# medium: http://lintcode.com/zh-cn/problem/construct-binary-tree-from-inorder-and-postorder-traversal/
