# coding: utf-8

class Solution:
    # @param {TreeNode} root, the root of binary tree.
    # @return {int} The maximum amount of money you can rob tonight
    def houseRobber3(self, root):
        # write your code here
        # 递归！比较该节点抢和不抢的最大值。
        return max(self._houseRobber3(root))

    def _houseRobber3(self, root):
        if not root:
            return (0, 0)
        rob_left = self._houseRobber3(root.left)
        rob_right = self._houseRobber3(root.right)
        not_rob = rob_left[1] + rob_right[1] + root.val
        rob = max(rob_left) + max(rob_right)
        return (not_rob, rob)

# medium: http://lintcode.com/zh-cn/problem/house-robber-iii/
