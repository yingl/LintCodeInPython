# coding: utf-8

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        self.quickSort(A, 0, len(A))

    def quickSort(self, array, start, end):
        if start < end:
            pivot_index = self.partition(array, start, end)  # 左右分区
            self.quickSort(array, start, pivot_index)
            self.quickSort(array, pivot_index + 1, end)

    def partition(self, array, start, end):
        pivot_index = start
        pivot = array[pivot_index]
        for i in xrange(start + 1, end):
            if array[i] < pivot:
                pivot_index += 1  # 每发现一个比pivot小的元素，意味着pivot的位置往后移一位。
                if pivot_index != i:
                    array[pivot_index], array[i] = array[i], array[pivot_index]
        array[start], array[pivot_index] = array[pivot_index], array[start]
        return pivot_index

# easy: http://lintcode.com/zh-cn/problem/sort-integers-ii/
