class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, str):
        # Write your code here
        count = 0
        ret = []
        for c in str:
            if (c < '0') or (c > '9'):
                ret.append(c)
            else:
                count += int(c)
        ret.sort()
        if count != 0:
            ret.append(count.__str__())
        return ''.join(ret)
        
easy: https://www.lintcode.com/problem/rearrange-a-string-with-integers
