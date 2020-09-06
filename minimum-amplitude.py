class Solution:
    """
    @param A: a list of integer
    @return: Return the smallest amplitude
    """
    def MinimumAmplitude(self, A):
        # write your code here
        ret = 0
        A.sort()
        if len(A) > 3:
            i = len(A) - 1
            ret = A[i] - A[3] # 去掉前面3个
            ret = min(A[i - 1] - A[2], ret) # 比较去掉前面2个和最后1个的情况
            ret = min(A[i - 2] - A[1], ret) # 比较去掉前面1个和最后2个的情况
            ret = min(A[i - 3] - A[0], ret) # 比较去掉最后3个的情况
        return ret
        
# easy: https://www.lintcode.com/problem/minimum-amplitude/
