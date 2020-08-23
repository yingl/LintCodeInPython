class Solution:
    """
    @param offset: the number of items that the customer has viewed
    @param n: the number of items that can be displayed on a page
    @param len1: the length of L1
    @param len2: the length of L2
    @return: returns the intervals of goods displayed in L1 and L2
    """
    def ProductList(self, offset, n, len1, len2):
        # write your code here
        ret = [0, 0, 0, 0]
        total = offset + n
        if offset < len1:
            ret[0] = offset
            if total <= len1:
                ret[1] = total
            else:
                ret[1] = len1
        else:
            ret[0] = len1
            ret[1] = len1
        if total >= len1:
            if offset >= len1:
                ret[2] = offset - len1
            print(total, len1)
            total -= len1
            if total > len2:
                total = len2
            ret[3] = total
        return ret
        
# easy: https://www.lintcode.com/problem/product-list/
