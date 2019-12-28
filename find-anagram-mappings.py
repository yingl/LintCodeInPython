class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        # Write your code here
        ret = []
        di = {}
        for i in range(len(B)):
            di[B[i]] = i
        for i in A:
            ret.append(di[i])
        return ret
        
# easy: https://www.lintcode.com/problem/find-anagram-mappings/
