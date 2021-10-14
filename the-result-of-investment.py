class Solution:
    """
    @param funds: The investment each time
    @param a: The initial funds of A
    @param b: The initial funds of B
    @param c: The initial funds of C
    @return: The final funds
    """
    def getAns(self, funds, a, b, c):
        # Write your code here
        r = [a, b, c]
        for f in funds:
            v = r[0]
            p = 0
            for i in [1, 2]:
                if r[i] < v:
                    v = r[i]
                    p = i
            r[p] += f
        return r
      
# easy: https://www.lintcode.com/problem/1615/
