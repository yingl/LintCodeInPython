# coding: utf-8

class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        if n == 0:
            return [None]
        # return self.dfs([i + 1 for i in xrange(n)])
        array = [i + 1 for i in xrange(n)]
        return self._generateTrees(array, 0, len(array))

    def _generateTrees(self, array, start, end):
        trees = []
        for i in xrange(start, end):
            left_trees, right_trees = [], []
            if i > 0:
                left_trees = self._generateTrees(array, start, i)   # 生成所有的左子树
            if i < (end - 1):
                right_trees = self._generateTrees(array, i + 1, end)    # 生成所有的右子树
            left_trees = [None] if not left_trees else left_trees
            right_trees = [None] if not right_trees else right_trees
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(array[i])
                    root.left, root.right = left_tree, right_tree
                    trees.append(root)
        return trees

# medium: http://lintcode.com/zh-cn/problem/unique-binary-search-trees-ii/
