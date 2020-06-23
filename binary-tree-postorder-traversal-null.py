"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        ret = []
        if root:
            s1, s2 = [root], []
            while s1:
                node = s1.pop()
                s2.append(node)
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)
            while s2:
                ret.append(s2.pop().val)
        return ret
        
# easy: https://www.lintcode.com/problem/binary-tree-postorder-traversal-null/
