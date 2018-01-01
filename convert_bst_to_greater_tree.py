# coding: utf-8

class Solution:
    """
    @param: root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        # print(root.val, root.left.val, root.right.val)
        # print(root.left.val, root.left.left.val, root.left.right.val)
        # 传进来的树可能不符合二叉搜索树的规则，但还是按规矩处理。
        #       [1]
        #   [2]     [3]
        # [4] [5] [6] [7]
        #
        # [1] = [1] + ([3] + [6] + [7]) = 17
        # [3] = [3] + [7] = 10
        # [6] = [6] + [10](from [3]) = 16
        # [7] = 7
        # [2] = [2] + [5] + [17](from [1]) = 24
        # [4] = [4] + [24](from [2]) = 28
        # [5] = [5] + [17](from [1]) = 22
        # {17, 24, 10, 28, 22, 16, 7}
        '''
        # 先使用递归方法实现
        Solution._convert(root, [0]) # 使用list传引用简化代码
        return root
        '''
        # 非递归做法
        if root:
            sum_ = 0
            stack = []
            p = root
            while p or (len(stack) > 0):
                while p:
                    stack.append(p)
                    p = p.right
                p = stack[-1]
                stack.pop()
                p.val += sum_
                sum_ = p.val
                p = p.left
        return root

    @staticmethod
    def _convert(root, sum_):
        if root:
            Solution._convert(root.right, sum_)
            root.val += sum_[0]
            sum_[0] = root.val
            Solution._convert(root.left, sum_)

# easy: http://lintcode.com/zh-cn/problem/convert-bst-to-greater-tree/
