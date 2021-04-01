"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root1: the first tree
    @param root2: the second tree
    @return: returns whether the leaf sequence is the same
    """
    def leafSimilar(self, root1, root2):
        # write your code here.
        r1, r2 = [], []
        self.dfs(r1, [root1])
        self.dfs(r2, [root2])
        return r1 == r2

    def dfs(self, leafs, nodes):
      while nodes:
        node = nodes.pop()
        if not (node.left or node.right):
          leafs.append(node.val)
        else:
          if node.left:
            nodes.append(node.left)
          if node.right:
            nodes.append(node.right)
            
# easy: https://www.lintcode.com/problem/leaf-similar-trees/
