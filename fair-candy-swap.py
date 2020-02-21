class Solution:
    """
    @param A: an array
    @param B: an array
    @return: an integer array
    """
    def fairCandySwap(self, A, B):
        # Write your code here.
        # 题目的关键是只需要交换一个，且答案一定存在。
        sum_a, sum_b = sum(A), sum(B)
        target = int((sum_a + sum_b) / 2) # 最终手里的数量
        diff = int((sum_a - sum_b) / 2)
        for a in A:
            for b in B:
                if a - b == diff:
                    return [a, b]

# easy: https://www.lintcode.com/problem/fair-candy-swap/
