class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, inputA, inputB):
        # Write your code here
        aa = []
        bb = []
        for c in inputA:
            if c != '<':
                aa.append(c)
            else:
                if aa:
                    aa.pop()
        for c in inputB:
            if c != '<':
                bb.append(c)
            else:
                if bb:
                    bb.pop()
        return 'YES' if aa == bb else 'NO'
      
# easy: https://www.lintcode.com/problem/823/
