# coding: utf-8

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        step = 0
        for i in range(0, len(A)):
            if A[i] == elem:
                step += 1
            else:
                A[i - step] = A[i]
        return len(A) - step

# easy: http://lintcode.com/zh-cn/problem/remove-element/
