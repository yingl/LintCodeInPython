class Solution:
    """
    @param s: string
    @return: sort string in lexicographical order
    """
    def sorting(self, s):
        # write your code here
        ns = s.split(',')
        ns.sort()
        return ','.join(ns)
        
# easy: https://www.lintcode.com/problem/string-sorting/
