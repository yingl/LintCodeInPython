class Solution:
    """
    @param sales: a integer array
    @return: return a Integer
    """
    def BalancedSalesArray(self, sales):
        # write your code here
        ls, rs = [], []
        for i in sales:
            if not ls:
                ls.append(i)
            else:
                ls.append(ls[-1] + i)
        for i in range(len(sales) - 1, -1, -1):
            if not rs:
                rs.append(sales[i])
            else:
                rs.append(rs[-1] + sales[i])
        for i in range(len(sales)):
            if ls[i] == rs[len(sales) - i - 1]:
                return i
        return -1
      
# easy: https://www.lintcode.com/problem/1793/
