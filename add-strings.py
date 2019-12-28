class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        ret = []
        l1, l2 = len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        step = 0
        for i in range(min(l1, l2)):
            v = (ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0')) + step
            if v >= 10:
                ret.append(chr(v - 10 + ord('0')))
                step = 1
            else:
                ret.append(chr(v + ord('0')))
                step = 0
        start, num = l1, num2
        if l2 < l1:
            start, num = l2, num1
        for i in range(start, len(num)):
            v = (ord(num[i]) - ord('0')) + step
            if v >= 10:
                ret.append(chr(v - 10 + ord('0')))
                step = 1
            else:
                ret.append(chr(v + ord('0')))
                step = 0
        if step == 1:
            ret.append('1')
        return ''.join(ret[::-1])

# easy: https://www.lintcode.com/problem/add-strings/
