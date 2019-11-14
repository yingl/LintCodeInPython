class Solution:
    """
    @param n: a Integer
    @return: the first n-line Yang Hui's triangle
    """
    def calcYangHuisTriangle(self, n):
        # write your code here
        if n == 0:
            return []
        else:
            ret = [[1]]
            for i in range(1, n):
                prev_level = ret[-1]
                new_level = [1]
                for i in range(len(prev_level) - 1):
                    new_level.append(prev_level[i] + prev_level[i + 1])
                new_level.append(1)
                ret.append(new_level)
            return ret

# easy: http://lintcode.com/zh-cn/problem/yang-hui-triangle/
