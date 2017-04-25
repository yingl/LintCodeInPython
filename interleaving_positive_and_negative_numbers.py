# coding: utf-8

class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def rerange(self, A):
        # write your code here
        '''
        偶数情况：XXXX,OOOO
        - XXXO,OOXO (第4个位置的X与第3个位置的O换）
        - XOXO,XOXO (第2个位置的X与第1个位置的O换）
        奇数情况：XXXXXXX,OOOOOOO
        - XXXXXOX,OOOOOXO（第6个位置的X与第6个位置的O互换）
        - XXXOXOX,OOOXOXO（第4个位置的X与第4个位置的O互换）
        - XOXOXOX,OXOXOXO（第2个位置的X与第2个位置的O互换）
        X和O，数量比较多的排前面。
        对于X,XXX,OOO的情况，不考虑前面多余的O，得到X,XOXOXO，然后对多余X后面部分反转得到X,OXOXOX。
        '''
        A.sort()
        neg_count, pos_count = 0, 0
        for n in A:
          if n < 0:
            neg_count += 1
          else:
            pos_count += 1
        if pos_count > neg_count:
            A.reverse()
        # TODO
        shift = abs(neg_count - pos_count)
        steps = min(neg_count, pos_count)
        first_start, first_end = shift, shift + steps - 1
        second_start, second_end = shift + steps, len(A) - 2  # 后半部分的循环总是从倒数第2个元素开始
        if (steps % 2) == 1:  # 做起点修正
            first_end -= 1
        while second_end >= second_start:
            A[first_end], A[second_end] = A[second_end], A[first_end]
            first_end -= 2
            second_end -= 2
        if shift > 0:
            start, end = shift, len(A) - 1
            while start < end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1

# medium: http://lintcode.com/zh-cn/problem/interleaving-positive-and-negative-numbers/
