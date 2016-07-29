# -*- coding: utf-8 -*-

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        for i in xrange(0, len(A)):
            for j in xrange(i, len(A)):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]