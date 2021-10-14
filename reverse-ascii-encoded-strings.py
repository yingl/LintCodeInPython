class Solution:
    """
    @param encodeString: an encode string
    @return: a reversed decoded string
    """
    def reverseAsciiEncodedString(self, encodeString):
        # Write your code here
        r = []
        for i in range(len(encodeString) - 1, 0, -2):
            v0 = int(encodeString[i])
            v1 = int(encodeString[i - 1])
            c = chr(v1 * 10 + v0)
            r.append(c)
        return ''.join(r)
      
# easy: https://www.lintcode.com/problem/1781/
