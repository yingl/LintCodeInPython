class Solution:
    """
    @param trees: the positions of trees.
    @param d: the minimum beautiful interval.
    @return: the minimum number of trees to remove to make trees beautiful.
    """
    def treePlanning(self, trees, d):
        # write your code here.
        left = [trees[0]]
        prev = left[0]
        for i in range(1, len(trees)):
            if (trees[i] - prev) >= d:
                left.append(trees[i])
                prev = trees[i]
        return len(trees) - len(left)

# easy: https://www.lintcode.com/problem/treeplanning/
