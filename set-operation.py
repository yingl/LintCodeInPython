class Solution:
    """
    @param A: The set A
    @param B: The set B
    @return: Return the size of three sets
    """
    def getAnswer(self, A, B):
        # Write your code here
        a, b = set(A), set(B)
        return [len(a | b), len(a & b), len(a - b)]
      
# easy: https://www.lintcode.com/problem/1471/
