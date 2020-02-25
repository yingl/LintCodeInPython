"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param root: the root of the tree
    @return: post order of the tree
    """
    def postorder(self, root):
        # write your code here
        ret = []
        self._postorder(root, ret)
        return ret

    def _postorder(self, root, ret):
        if root:
            for n in root.neighbors:
                self._postorder(n, ret)
            ret.append(root.label)

# easy: https://www.lintcode.com/problem/n-ary-tree-postorder-traversal/
