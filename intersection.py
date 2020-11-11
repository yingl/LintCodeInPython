class Solution:
    """
    @param a: first sequence
    @param b: second sequence
    @return: return ans
    """
    def Intersection(self, a, b):
        # write your code here
        ret = []
        prev_j = 0
        for i in range(len(a)):
            _a = a[i]
            for j in range(prev_j, len(b)):
                _b = b[j]
                if _b[0] > _a[1]:
                    break
                if self._intersection(_a, _b):
                    ret.append([i, j])
                    prev_j = j
        return ret
        
    def _intersection(self, a, b):
        v0_0, v0_1 = a[0], a[1]
        v1_0, v1_1 = b[0], b[1]
        return not ((v0_1 < v1_0) or (v0_0 > v1_1) or (v1_0 > v0_1) or (v1_1 < v0_0))
        
# easy: https://www.lintcode.com/problem/intersection/
