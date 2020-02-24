"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param root: the tree
    @return: pre order of the tree
    """
    def preorder(self, root):
        # write your code here
        ret = []
        self._preorder(root, ret)
        return ret
        
    def _preorder(self, root, ret):
        if root:
            ret.append(root.label)
            for node in root.neighbors:
                self._preorder(node, ret)

# easy: https://www.lintcode.com/problem/n-ary-tree-preorder-traversal/
