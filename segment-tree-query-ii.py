# coding: utf-8

class Solution: 
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The count number in the interval [start, end] 
    def query(self, root, start, end):
        # write your code here
        ret = 0
        if root:
            if start < root.start:  # 收缩start、end范围
                start = root.start
            if end > root.end:
                end = root.end
            if (start == root.start) and (end == root.end):
                ret = root.count
            else:
                if root.left: # 左子树存在
                    if start <= root.left.end:  # 可以去左子树继续
                        ret = self.query(root.left, start, end)
                        if root.right and (end >= root.right.start):  # 判断是否需要去右子树
                            ret += self.query(root.right, start, end)
                    elif root.right and (start >= root.right.start):  # start是否满足进入右节点的要求
                        ret += self.query(root.right, start, end)
        return ret

# medium: http://lintcode.com/zh-cn/problem/segment-tree-query-ii/
