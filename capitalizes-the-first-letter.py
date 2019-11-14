class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        # Write your code here
        ret = list(s)
        start = 0
        while start < len(ret):
            if ret[start] == ' ':
                start += 1
            else:
                break
        is_first = True
        for i in range(start, len(ret)):
            if is_first and ret[i] != ' ':
                ret[i] = ret[i].upper()
                is_first = False
            elif ret[i] == ' ':
                is_first = True
        return ''.join(ret)

# easy: https://www.lintcode.com/problem/capitalizes-the-first-letter/
