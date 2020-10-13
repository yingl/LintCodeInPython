class Solution:
    """
    @param s: a string for this game 
    @return: return whether Alice can win this game
    """
    def stringGame(self, s):
        # Write your code here
        # Nim模型是拿最后一块石子的赢，但这属于反Nim模型。
        # 先手必胜的条件：
        # - 所有堆的石子数均=1，且有偶数堆。
        # - 至少有一个堆的石子的数量大于1，且石子堆的异或和不等与0。
        # 证明网上有。
        cnt = 0
        xor = 0
        di = {}
        for c in s:
            if c not in di:
                di[c] = 0
            di[c] += 1
        for k, v in di.items():
            if v == 1:
                cnt += 1
            xor ^= v
        if cnt == len(s):
            return (cnt % 2) == 0
        return xor > 0
        
# easy: https://www.lintcode.com/problem/string-game/
