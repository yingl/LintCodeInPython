# coding: utf-8

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        import collections
        paths = collections.deque([(start, 1)]) # start做为起始单词
        while paths:
            path = paths.popleft()
            word, length = path[0], path[1]
            if word == end:
                return length # 匹配成功，返回变换长度。
            for i in xrange(len(word)):
                left, right = word[0:i], word[i + 1:]
                # 遍历生成变换可生成的单词
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] != ch:
                        new_word = left + ch + right
                        if new_word in dict:
                            paths.append((new_word, length + 1))
                            dict.remove(new_word)
        return 0

# medium: http://lintcode.com/zh-cn/problem/word-ladder/
