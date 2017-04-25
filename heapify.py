# coding: utf-8

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        '''
        为什么从1/2的位置从后往前遍历？
        因为对于堆中下标为i的元素，子节点下标为i * 2 + 1和i * 2 + 2，
        对于下标大于1/2位置的元素一定是叶子节点，无须做向下调整。
        '''
        for i in xrange((len(A) - 1) / 2, -1, -1):
            while i < len(A):
                left, right = i * 2 + 1, i * 2 + 2
                min_pos = i
                if (left < len(A)) and (A[left] < A[min_pos]):
                    min_pos = left
                if (right < len(A)) and (A[right] < A[min_pos]):
                    min_pos = right
                if min_pos != i:    # 调整A[i]元素位置，继续向下调整。
                    A[i], A[min_pos] = A[min_pos], A[i]
                    i = min_pos
                else:   # min_pos没变，A[i]无须调整，结束循环。
                    break

# medium: http://lintcode.com/zh-cn/problem/heapify/
