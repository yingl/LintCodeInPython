# coding: utf-8

class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    def reversePairs(self, A):
        # Write your code here
        '''
        用二分法做从大到小的归并排序。
        对于已归并的a1和a2，先更新逆序数，再排序。
        '''
        self.tmp = [0] * len(A)
        return self._reversePairs(A, 0, len(A) - 1)

    def _reversePairs(self, A, start, end):
        pairs = 0
        if start < end:
            mid = (start + end) / 2
            pairs = self._reversePairs(A, start, mid)
            pairs += self._reversePairs(A, mid + 1, end)
            pairs += self.merge(A, start, end)
        return pairs

    def merge(self, A, start, end):
        pairs = 0
        mid = (start + end) / 2
        i, j = start, mid + 1
        k = start
        while (i <= mid) and (j <= end):
            if A[i] > A[j]:
                pairs += (end - j + 1)  # j以及之后的元素数量
                self.tmp[k] = A[i]
                i += 1
            else:
                self.tmp[k] = A[j]
                j += 1
            k += 1
        while i <= mid:
            self.tmp[k] = A[i]
            i += 1
            k += 1
        while j <= end:
            self.tmp[k] = A[j]
            j += 1
            k += 1
        for i in xrange(start, end + 1):
            A[i] = self.tmp[i]
        return pairs

# medium: http://lintcode.com/zh-cn/problem/reverse-pairs/
