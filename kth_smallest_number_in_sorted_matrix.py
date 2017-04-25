# coding: utf-8

class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        heap = []
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if len(heap) < k: # 先把堆填满
                    heap.append(matrix[i][j])
                    self.adjustUp(heap) # 因为新元素添加在尾部，只要做向上调整。
                    j += 1  # 下一列
                else:
                    if matrix[i][j] < heap[0]:
                        heap[0] = matrix[i][j]  # 因为matrix[i][j]更小，替换原来的根节点。
                        self.adjustDown(heap) # 因为根节点更新了，所以做向下调整。
                        j += 1  # 下一列
                    else:
                        '''
                        这段很重要，因为matrix[i][j] > heap[0]，
                        所以对于后面的所有列，不肯能会出现matrix[i][j'] < heap[0]，
                        直接从下一行开始，不然数据量大会超时。
                        '''
                        break
            i += 1  # 下一行
        return heap[0]

    def adjustUp(self, heap):
        i = len(heap) - 1
        while i >= 0:
            parent = (i - 1) / 2
            if (parent >= 0) and (heap[parent] < heap[i]):
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break

    def adjustDown(self, heap):
        i = 0
        while i < len(heap):
            left, right, max_pos = i * 2 + 1, i * 2 + 2, i
            if (left < len(heap)) and (heap[left] > heap[max_pos]):
                max_pos = left
            if (right < len(heap)) and (heap[right] > heap[max_pos]):
                max_pos = right
            if max_pos != i:
                heap[i], heap[max_pos] = heap[max_pos], heap[i]
                i = max_pos
            else:
                break

# medium: http://lintcode.com/zh-cn/problem/kth-smallest-number-in-sorted-matrix/
