# coding: utf-8

class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        # 最简单的思路是三重循环，但是有效率问题。
        # 参考了网上的做法，可以改为二重循环加二分。
        # 但是Python的执行效率有问题，翻译成Java或C++可过。
        ret = 0
        S.sort()
        for i in xrange(len(S)): # 最短边
            for j in xrange(i + 2, len(S)): # 最长边
                # 用二分法确认第三条边的范围
                # 三角形的三条边满足如下条件：
                # - a - b < c
                # - c < a + b
                target = S[j] - S[i]
                l, r = i + 1, j
                while l < r:
                    mid = int((l + r) / 2)
                    if S[mid] > target:
                        # 满足a - b < c，所以该边和右侧所有的边都满足
                        r = mid
                    else:
                        # a - b >= c，所以该边和左侧所有的边不包含在内
                        l = mid + 1
                ret += (j - l)
        return ret

# medium: http://lintcode.com/zh-cn/problem/triangle-count/
