class Solution:
    """
    @param Message: the string xiao Q sent to xiao A.
    @return: the string after decompress
    """
    def DecompressString(self, Message):
        #
        ret = []
        stack = []
        i = 0
        s = ''
        while i < len(Message):
            c = Message[i]
            i += 1
            if (c != '[') and (c != ']') and (c != '|'):
                s += c
            else:
                if s:
                    stack.append(s)
                s = ''
                stack.append(c)
        if s:
            stack.append(s)
        for s in stack:
            if s != ']':
                ret.append(s)
            elif s == ']':
                r0 = ret.pop()
                r1 = ret.pop()
                while r1 != '|':
                    r0 = r1 + r0
                    r1 = ret.pop()
                r2 = 0
                if r1 == '|':
                    r2 = int(ret.pop())
                ret.pop() # 弹出'['
                if r2 == 0:
                    ret.append(r1 + r0)
                else:
                    ret.append(r0 * r2)
        return ''.join(ret)
        
# easy: https://www.lintcode.com/problem/decrypt-the-string/
