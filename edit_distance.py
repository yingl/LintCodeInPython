# coding: utf-8

class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        self.cache = [[-1] * len(word2) for i in xrange(len(word1))]
        return self._minDistance(word1, 0, word2, 0)

    def _minDistance(self, word_1, start_1, word_2, start_2):
        if start_1 >= len(word_1):
            return len(word_2) - start_2
        elif start_2 >= len(word_2):
            return len(word_1) - start_1
        if self.cache[start_1][start_2] == -1:
            # 假设通过插入一个与另一方相同位置一样的字符
            dist_1 = 1 + min(self._minDistance(word_1, start_1 + 1, word_2, start_2), \
                      self._minDistance(word_1, start_1, word_2, start_2 + 1))
            # 相同位置如果不同，做一次字符改变，继续处理后面的字符串。
            dist_2 = self._minDistance(word_1, start_1 + 1, word_2, start_2 + 1)
            if word_1[start_1] != word_2[start_2]:
                dist_2 += 1
            self.cache[start_1][start_2] = min(dist_1, dist_2)
        return self.cache[start_1][start_2]

# medium: http://lintcode.com/zh-cn/problem/edit-distance/
