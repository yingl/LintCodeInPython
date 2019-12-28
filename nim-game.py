class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def canWinNim(self, n):
        # Write your code here
        return (n % 4) != 0
        
# easy: https://www.lintcode.com/problem/nim-game/
