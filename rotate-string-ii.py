class Solution:
    """
    @param str: A String
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        li = list(str)
        ls, rs = -1, -1
        right %= len(li)
        left %= len(li)
        if right > left:
            rs = right - left
        elif left > right:
            ls = left - right
        shift = -1
        if ls > 0:
            shift = ls
        elif rs > 0:
            shift = len(li) - rs
        if shift > 0:
            self.reverse(li, 0, shift)
            self.reverse(li, shift, len(li))
            self.reverse(li, 0, len(li))
        return ''.join(li)
        
    def reverse(self, li, start, end):
        end = end - 1
        while start < end:
            li[start], li[end] = li[end], li[start]
            start += 1
            end -= 1
        
# easy: https://www.lintcode.com/problem/rotate-string-ii/
