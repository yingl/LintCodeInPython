class Solution:
    """
    @param S: 
    @return: nothing
    """
    def  toGoatLatin(self, S):
        # 
        words = S.split() # 偷懒做法
        for i in range(len(words)):
            word = words[i]
            tail = 'ma' + 'a' * (i + 1)
            if word[0] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                words[i] = word + tail
            else:
                words[i] = word[1:] + word[0] + tail
        return ' '.join(words)

# easy: https://www.lintcode.com/problem/goat-latin/
