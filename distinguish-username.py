class Solution:
    """
    @param names: a string array
    @return: the string array
    """
    def DistinguishUsername(self, names):
        # Write your code here
        r = []
        m = {}
        for n in names:
            if n not in m:
                m[n] = [1, 0]
            else:
                m[n][0] += 1
        for n in names:
            if m[n][0] == 1:
                r.append(n)
            else:
                if m[n][1] == 0:
                    r.append(n)
                else:
                    r.append(n + str(m[n][1]))
                m[n][1] += 1
        return r
      
# easy: https://www.lintcode.com/problem/1789/
