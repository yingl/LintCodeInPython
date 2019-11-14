# coding: utf-8

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        if not root:
            return 0
        self.ret = -2147483648
        self._maxPathSum(root)
        return self.ret

    def _maxPathSum(self, root):
        if not root:
            return 0
        left_sum = self._maxPathSum(root.left)
        right_sum = self._maxPathSum(root.right)
        '''
        从以下值中比较获取最大值与self.ret比较并更新
        - root.val
        - root.val + max_left_sum
        - root.val + max_right_sum
        - root.val + max_left_sum + max_right_sum
        这个值是当前包含该节点的最大路径和
        '''
        sub_max = max(root.val + left_sum, root.val + right_sum)
        sub_max = max(sub_max, root.val)
        sub_max = max(sub_max, root.val + left_sum + right_sum)
        if sub_max > self.ret:
            self.ret = sub_max
        '''
        返回值应当是以下值中比较获取最大，因为路径要向上延伸：
        - root.val
        - root.val + max_left_sum
        - root.val + max_right_sum
        '''
        return max(max(root.val + left_sum, root.val + right_sum), root.val)

# medium: http://lintcode.com/zh-cn/problem/binary-tree-maximum-path-sum/
