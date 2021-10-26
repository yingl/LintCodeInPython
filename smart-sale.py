class Solution:
    """
    @param ids: ID number of items
    @param m: The largest number of items that can be remove
    @return: the result of the min item
    """
    def minItem(self, ids, m):
        # write your code here
        r = 0
        di = {}
        for i in ids:
            if i not in di:
                di[i] = 1
                r += 1
            else:
                di[i] += 1
        s = sorted(di.values())
        for i in s:
            if i > m:
                return r
            else:
                m -= i
                r -= 1
        return r
      
# medium: https://www.lintcode.com/problem/1914
