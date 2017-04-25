# coding: utf-8

class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if (not root) or (root == A) or (root == B):
            return root
        left = self.lowestCommonAncestor(root.left, A, B)   # 在左子树找AB的最近公共祖先
        right = self.lowestCommonAncestor(root.right, A, B) # 在右子树找AB的最近公共祖先
        '''
        如果left和right都不会空，说明A、B分别在root的左、右子树，root是最近公共祖先。
        如果A、B都在root的左子树，那么right肯定为空，最近公共祖先肯定在左子树中。所以left就是返回最近公共祖先。
        '''
        if left and right:
            return root
        else:
            return left if left else right

# medium: http://lintcode.com/zh-cn/problem/lowest-common-ancestor/
