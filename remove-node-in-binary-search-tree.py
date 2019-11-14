# coding: utf-8

class Solution:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def removeNode(self, root, value):
        # write your code here
        if not root:
            return
        if root.val == value:
            new_root = self.rebuildTree(root.left, root.right)
            # 不能简单的root等于new_root，因为是引用，必须修改值！！！
            if new_root:
                root.val = new_root.val
                root.left, root.right = new_root.left, new_root.right
            else:
                root = None
        elif root.val < value:
            self.removeNode(root.right, value)
        else:
            self.removeNode(root.left, value)
        return root
            
    def rebuildTree(self, left, right): # 根据左右子树生成一棵新的树
        if not left:
            return right
        if not right:
            return left
        '''
        利用递归把left的左右子树生成一颗新树，然后left.left指向它，
        left.right继续指向原来的子树不用变化。
        '''
        left.left = self.rebuildTree(left.left, left.right)
        left.right = right
        return left

# hard: http://lintcode.com/zh-cn/problem/remove-node-in-binary-search-tree/
