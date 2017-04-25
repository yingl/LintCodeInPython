# coding: utf-8

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        i = 1
        dists = [triangle[0][0]]
        while i < len(triangle):
            new_dists = [triangle[i][0] + dists[0]]
            for j in xrange(1, len(triangle[i])):
                '''
                dists为上一层记录，
                new_dists保存根据上一层记录计算出的当前层数据。
                '''
                if j == (len(triangle[i]) - 1):
                    new_dists.append(triangle[i][-1] + dists[-1])
                else:
                    new_dists.append(triangle[i][j] + min(dists[j - 1], dists[j]))
            dists = new_dists
            i += 1
        return min(dists)

# easy: http://lintcode.com/zh-cn/problem/triangle/
