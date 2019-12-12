class Solution:
    """
    @param root: the root
    @return: the same tree where every subtree (of the given tree) not containing a 1 has been removed
    """
    def pruneTree(self, root):
        # Write your code here
        if not root:
            return None
        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)
        if root.left == None and root.right == None:
            if root.val == 0:
                return None
        return root

# easy: https://www.lintcode.com/problem/binary-tree-pruning/
