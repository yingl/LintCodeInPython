# coding: utf-8

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A:
            start, end = 0, len(A)
            while start < end:
                mid = (start + end) / 2
                if A[mid] < target:
                    start += 1
                elif A[mid] > target:
                    end = mid
                else:
                    break
            # 判断mid位置
            if A[mid] > target:
                return mid
            elif A[mid] < target:
                return mid + 1
            else:
                # 等于的情况要找到第一个插入位置
                for i in xrange(mid - 1, -1, -1):
                    if A[i] < target:
                        return i + 1
        return 0

# easy: http://lintcode.com/zh-cn/problem/search-insert-position/
