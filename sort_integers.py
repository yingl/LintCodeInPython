# coding: utf-8

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]

# entry: http://www.lintcode.com/problem/sort-integers
