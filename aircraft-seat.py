class Solution:
    """
    @param N:  the number of rows
    @param S: a list of reserved seats
    @return: nothing
    """
    def solution(self, N, S):
        # Write your code here.
        # 放4个人只有以下三种方案：BCDE DEFG FGHJ
        ret = 0
        occupied = set(S.split(' '))
        for i in range(1, N + 1):
            SB = str(i) + 'B'
            SC = str(i) + 'C'
            SD = str(i) + 'D'
            SE = str(i) + 'E'
            SF = str(i) + 'F'
            SG = str(i) + 'G'
            SH = str(i) + 'H'
            SI = str(i) + 'I'
            SJ = str(i) + 'J'
            if (SB not in occupied) and (SC not in occupied) and (SD not in occupied) and (SE not in occupied):
                ret += 1
                occupied.add(SE) # 占坑
            if (SD not in occupied) and (SE not in occupied) and (SF not in occupied) and (SG not in occupied):
                ret += 1
                occupied.add(SG)
            if (SF not in occupied) and (SG not in occupied) and (SH not in occupied) and (SI not in occupied):
                ret += 1
        return ret
        
# easy: https://www.lintcode.com/problem/aircraft-seat/
