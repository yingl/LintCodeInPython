class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        # write your code here
        vs = []
        i = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for c in num2:
            vs.append(self._multiply(num1, int(c), i))
            i += 1
        ret = vs[0]
        for i in range(1, len(vs)):
            ret = self._add(ret, vs[i])
        for i in range(len(ret) - 1, -1, -1):
            if ret[i] == '0':
                ret.pop()
            else:
                break
        ret = ret[::-1]
        if not ret:
            return '0'
        else:
            return ''.join(ret)

    def _multiply(self, num1, k, zs):
        ret = ['0'] * zs
        val = []
        step = 0
        for i in num1:
            i = int(i)
            v = i * k + step
            val.append(str(v % 10))
            step = int(v / 10)
        if step:
            val.append(int(step))
        return ret + val
        
    def _add(self, num1, num2): # num1 <= num2, already reversed
        ret = []
        step = 0
        for i in range(len(num1)):
            v1 = int(num1[i])
            v2 = int(num2[i])
            v = v1 + v2 + step
            ret.append(str(v % 10))
            step = int(v / 10)
        for i in range(len(num1), len(num2)):
            v1 = int(num2[i])
            v = v1 + step
            ret.append(str(v % 10))
            step = int(v / 10)
        if step:
            ret.append('1')
        return ret
        
# medium: https://www.lintcode.com/problem/multiply-strings/
