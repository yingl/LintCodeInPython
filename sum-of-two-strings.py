class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        ret = []
        min_len = min(len(A), len(B))
        A = list(A) # 偷个懒，不然循环要从后往前写。
        B = list(B)
        A.reverse()
        B.reverse()
        for i in range(min_len):
            ret.append(str(int(A[i]) + int(B[i])))
        if len(A) > min_len:
            ret.extend(A[min_len:])
        elif len(B) > min_len:
            ret.extend(B[min_len:])
        ret.reverse()
        return ''.join(ret)
        
# easy: https://www.lintcode.com/problem/sum-of-two-strings/
