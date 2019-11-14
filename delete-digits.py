# coding: utf-8

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        '''
        既然是删除k个数字，可以理解为保留m个数字，m = len(A) - k.
        1. 扣掉最后m个数字，从前面找到一个最小数。
        2. 从前面最小数位置之后开始，扣掉最后m - 1个数字，再找一个最小数。
        3. 继续。。。
        '''
        digits = []
        start = 0
        k = len(A) - k
        while k > 0:
            min_index = self._min(A, start, k)
            digits.append(A[min_index])
            start = min_index + 1
            k -= 1
        ret = 0
        for d in digits:
            ret = ret * 10 + int(d)
        return ret
        
    def _min(self, A, start, k):  # 找到A[start:len(A) - k]里最小书的索引
        min_index = start
        for i in xrange(start + 1, len(A) - k + 1):
            if A[i] < A[min_index]:
                min_index = i
        return min_index

# medium: http://lintcode.com/zh-cn/problem/delete-digits/
