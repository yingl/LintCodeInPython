# coding: utf-8

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        start, end, _k = 0, len(A), k
        while True:
            ret, ret_index = self.partition(A, start, end)
            if ret_index != k:
                if ret_index > k:
                    start = len(A) - ret_index + 1
                else:
                    end = len(A) - ret_index
            else:
                return ret

    '''
    因为1/2 + 1/4 + ... + 1/2^n = 1，
    所以最终是O(n)的复杂度。
    '''
    def partition(self, array, start, end):
        ret, ret_index = array[start], start
        for i in xrange(start + 1, end):
            if array[i] < ret:
                ret_index += 1
                if ret_index != i:
                    array[ret_index], array[i] = array[i], array[ret_index]
        array[start], array[ret_index] = array[ret_index], array[start]
        return ret, len(array) - ret_index  # 如果不减就是第x + 1小！

# medium: http://lintcode.com/zh-cn/problem/kth-largest-element/
