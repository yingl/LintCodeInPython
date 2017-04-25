# coding: utf-8

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        steps = 0
        i = 0
        while i < len(A):
            number = A[i]
            A[i - steps] = number
            j = i + 1
            while (j < len(A)) and (A[j] == number):
                steps += 1
                j += 1
            i = j
        return len(A) - steps

# easy: http://lintcode.com/zh-cn/problem/remove-duplicates-from-sorted-array/
