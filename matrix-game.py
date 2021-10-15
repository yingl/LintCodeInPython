class Solution:
    """
    @param grids: a integer matrix
    @return: return the difference between two people at last.
    """
    def MatrixGame(self, grids):
        # write your code here
        if not grids:
            return 0
        ms = []
        for c in range(len(grids[0])):
            m = grids[0][c]
            for r in range(1, len(grids)):
                if grids[r][c] > m:
                    m = grids[r][c]
            ms.append(m)
        ms.sort()
        r = 0
        af = True
        for i in range(len(ms) - 1, -1, -1):
            if af:
                r += ms[i]
            else:
                r -= ms[i]
            af = not af
        return abs(r)
      
# easy: https://www.lintcode.com/problem/1421/
