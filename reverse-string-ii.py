class Solution:
    """
    @param s: the string
    @param k: the integer k
    @return: the answer
    """
    def reverseStringII(self, s, k):
        # Write your code here.
        ret = []
        i = 0
        while i < len(s):
            ik, ikk = i + k, i + k * 2
            if ik > len(s):
                ik = len(s)
            for j in range(ik - i):
                ret.append(s[ik - 1 - j])
            j = ik
            if ikk > len(s):
                ikk = len(s)
            while j < ikk:
                ret.append(s[j])
                j += 1
            i = ikk
        return ''.join(ret)

            
# easy: https://www.lintcode.com/problem/1182/
