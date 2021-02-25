"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def levelSum(self, root, level):
        # write your code here
        ret = 0
        if root and (level > 0):
            ilevel = 1
            curr_nodes = [root]
            next_nodes = []
            while ilevel < level:
                for node in curr_nodes:
                    if node.left:
                        next_nodes.append(node.left)
                    if node.right:
                        next_nodes.append(node.right)
                ilevel += 1
                curr_nodes = next_nodes
                next_nodes = []
            for node in curr_nodes:
                ret += node.val
        return ret
      
# easy: https://www.lintcode.com/problem/binary-tree-level-sum/
