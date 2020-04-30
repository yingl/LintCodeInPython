"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: the tree after swapping
    """
    def bstSwappedNode(self, root):
        # write your code here
        nodes = []
        self.inorder(root, nodes)
        start, end = 0, len(nodes) - 1
        while start < len(nodes) - 1:
            if nodes[start].val < nodes[start + 1].val:
                start += 1
            else:
                break
        while end >= 1:
            if nodes[end].val > nodes[end - 1].val:
                end -= 1
            else:
                break
        if start < end:
            nodes[start].val, nodes[end].val = nodes[end].val, nodes[start].val
        return root

    def inorder(self, root, nodes):
        if root:
            if root.left:
                self.inorder(root.left, nodes)
            nodes.append(root)
            if root.right:
                self.inorder(root.right, nodes)
                
# medium: https://www.lintcode.com/problem/recover-binary-search-tree/
