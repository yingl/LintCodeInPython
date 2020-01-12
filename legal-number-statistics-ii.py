class Solution:
    """
    @param a: the array a
    @param q: the queries q
    @return: for each query, return the number of legal integers 
    """
    def getAns(self, a, q):
        # write your code here
        ret = []
        for _q in q:
            ret.append(0)
            for i in a:
                if (i >= _q[0]) and (i <= _q[1]):
                    ret[-1] += 1
        return ret
        
# easy: https://www.lintcode.com/problem/legal-number-statistics-ii/
