class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        # 先分区，负数再前，正数在后。
        start, end = 0, len(A) - 1
        while (start < end):
            while (start < end) and (A[start] < 0):
                start += 1
            while (end >= 0) and (A[end] > 0):
                end -= 1
            if (start < end):
                A[start], A[end] = A[end], A[start]
        cp, cn = 0, 0
        for i in A:
            if i > 0:
                cp += 1
            else:
                cn += 1
        start, end = 0, len(A) - 1
        if cn > cp: # 前面的负数比后面的正数多
            start += 1
        elif cn < cp: # 后面的正数比前面的负数多
            end -= 1
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 2
            end -= 2

# medium: http://lintcode.com/zh-cn/problem/interleaving-positive-and-negative-numbers/
