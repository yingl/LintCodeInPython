# coding: utf-8

class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        # write your code here
        A.sort()
        B.sort()
        i, j = 0, 0
        diff = abs(A[0] - B[0])
        while (i < len(A)) and (j < len(B)):
            diff = min(abs(A[i] - B[j]), diff)  # 更新差
            if B[j] < A[i]:
                '''
                因为B[j]小于A[i]，所以在B[j+]大于A[i]之前，
                差的绝对值不会大于abs(A[i] - B[j])。
                '''
                while (j < len(B)) and (B[j] <= A[i]):
                    diff = min(abs(A[i] - B[j]), diff)
                    j += 1
            elif A[i] < B[j]:
                # 与上面同理
                while (i < len(A)) and (A[i] <= B[j]):
                    diff = min(abs(A[i] - B[j]), diff)
                    i += 1
            else:
                if (i == (len(A) - 1)) and (j == (len(B) - 1)):
                    break
                elif i < (len(A) - 1):
                    i += 1
                else:
                    j += 1
        return diff

# medium: http://lintcode.com/zh-cn/problem/the-smallest-difference/
