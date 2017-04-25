# coding: utf-8

class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if n <= 0:
            return 0
        start, end = 1, n + 1
        while start < end:
            mid = (start + end) / 2
            if SVNRepo.isBadVersion(mid):
                end = mid   # 错误范围[start, mid]
            else:
                start = mid + 1 # 错误在后半部分
        return start

# medium: http://lintcode.com/zh-cn/problem/first-bad-version/
