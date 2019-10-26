class Solution:
    """
    @param s: the original string
    @return: the string without arbitrary spaces
    """
    def removeExtra(self, s):
        # write your code here
        ret = []
        for c in s:
            if not ret:
                if c != ' ':
                    ret.append(c)
            else:
                if c != ' ':
                    ret.append(c)
                else:
                    if c != ret[-1]:
                        ret.append(c)
        return ''.join(ret).rstrip()
                
# easy: https://www.lintcode.com/problem/remove-arbitrary-space/
