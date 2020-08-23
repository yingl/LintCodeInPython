class Solution:
    """
    @param queen: queen‘coordinate
    @param knight: knight‘coordinate
    @return: if knight is attacked please return true，else return false
    """
    def isAttacked(self, queen, knight):
        # write your code here
        ret = []
        xmark, ymark = zip(*queen)
        xmark = set(xmark)
        ymark = set(ymark)
        diffs_1 = set([])
        diffs_2 = set([])
        for q in queen:
            diffs_1.add(q[1] - q[0])
            diffs_2.add(q[0] + q[1])
        for k in knight:
            if k[0] in xmark:
                ret.append(True)
                continue
            if k[1] in ymark:
                ret.append(True)
                continue
            if ((k[1] - k[0]) in diffs_1) or ((k[0] + k[1]) in diffs_2):
                ret.append(True)
                continue
            ret.append(False)
        return ret
        
# easy: https://www.lintcode.com/problem/chess-game/
