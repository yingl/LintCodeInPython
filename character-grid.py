class Solution:
    """
    @param A: A string
    @param B: A string
    @return: A string array
    """
    def characterGrid(self, A, B):
        # write your code here.
        ret = [['.'] * len(A) for i in range(len(B))]
        row, col = len(A), len(B)
        di_a, di_b = {}, {}
        self.init_dict(di_a, A)
        self.init_dict(di_b, B)
        for c in A:
            if c in di_b:
                col = di_a[c]
                row = di_b[c]
                break
        for i in range(len(B)):
            if i == row:
                ret[i] = list(A)
        for i in range(len(B)):
            ret[i][col] = B[i]
        for i in range(len(B)):
            ret[i] = ''.join(ret[i])
        return ret

    def init_dict(self, di, s):
        for i in range(len(s)):
            if s[i] not in di:
                di[s[i]] = i # 是要记录第一次出现的位置就可以
                
# easy: https://www.lintcode.com/problem/character-grid/
