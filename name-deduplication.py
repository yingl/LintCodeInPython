class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        # write your code here
        ret = []
        s = set()
        for n in names:
            nl = n.lower()
            if nl not in s:
                s.add(nl)
                ret.append(nl)
        return ret
      
# easy: https://www.lintcode.com/problem/487
