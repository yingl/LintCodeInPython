class Solution:
    """
    @param bits: a array represented by several bits. 
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        # Write your code here
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return True
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return False

# easy: https://www.lintcode.com/problem/1-bit-and-2-bit-characters/
