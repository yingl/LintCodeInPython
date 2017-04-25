# coding: utf-8

class Solution: 
    """
    @param root, index, value: The root of segment tree and 
    @ change the node's value with [index, index] to the new given value
    @return: nothing
    """
    def modify(self, root, index, value):
        # write your code here
        # write your code here
        if (index < root.start) or (index > root.end):
            return
        elif (index == root.start) and (index == root.end):
            root.max = value
            return value
        else:
            # 在修改完叶子节点后，需要一级级向上修改当前节点的max。
            if root.left:
                if index <= root.left.end:
                    _max = self.modify(root.left, index, value)
                    if root.right:
                        root.max = max(_max, root.right.max)
                    else:
                        root.max = _max
            if root.right:
                if index >= root.right.start:
                    _max = self.modify(root.right, index, value)
                    if root.left:
                        root.max = max(_max, root.left.max)
                    else:
                        root.max = _max
            return root.max

# medium: http://lintcode.com/zh-cn/problem/segment-tree-modify/
