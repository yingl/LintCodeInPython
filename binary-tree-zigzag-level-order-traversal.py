# coding: utf-8

class Solution:
    """
    @param root: The root of binary tree.
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        ret = []
        if not root:
            return ret
        level = [root]  # 当前遍历层
        order = 1   # 顺序遍历
        while level:
            data = []
            new_level = []  # 下一次循环遍历层
            for node in level:
                data.append(node.val)
                if order == 1:  # 顺序的时候先访问左节点 
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)
                else:   # 逆序的时候先访问右节点
                    if node.right:
                        new_level.append(node.right)
                    if node.left:
                        new_level.append(node.left)
            order *= -1 # 反转访问顺序
            level = new_level
            level.reverse() # 殷雯访问顺序反转，该层的数据也要反转。
            ret.append(data)
        return ret

# medium: http://lintcode.com/zh-cn/problem/binary-tree-zigzag-level-order-traversal/
