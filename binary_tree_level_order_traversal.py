# coding: utf-8

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        ret = []
        level = [root]
        while level:
            ret.append([])
            new_level = []
            for node in level:
                ret[-1].append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level = new_level
        return ret

# easy: http://lintcode.com/zh-cn/problem/binary-tree-level-order-traversal/
