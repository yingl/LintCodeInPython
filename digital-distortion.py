class Solution:
    """
    @param A: the integer discrible in problem
    @return: the integer after distortion
    """
    def Distortion(self, A):
        #
        ret = []
        i, j = 0, len(A) - 1
        while i < j:
            ret.append(A[j])
            ret.append(A[i])
            j -= 1
            i += 1
        if i == j:
            ret.append(A[i])
        return ''.join(ret)
        
# easy: https://www.lintcode.com/problem/digital-distortion/
