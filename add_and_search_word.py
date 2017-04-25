# coding: utf-8

class TrieNode: # 参考implement_trie.py实现
  def __init__(self):
    # Initialize your data structure here.
    self.map = {}
    self.isLeaf = False

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        root = self.root
        for ch in word:
            if ch not in root.map:
                root.map[ch] = TrieNode()
            root = root.map[ch]
        root.isLeaf = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        return self.dfs_search(self.root, word, 0)

    def dfs_search(self, root, word, i):    # 实现search
        if (not root) or (i >= len(word)):
            return False
        for ch, trie in root.map.items():
            if (word[i] == ch) or (word[i] == '.'):
                if ((i + 1) == len(word)) and trie.isLeaf:
                    return True # 匹配完成
                else:   # 搜索下一层
                    if self.dfs_search(trie, word, i + 1):
                        return True
        return False

# medium: http://lintcode.com/zh-cn/problem/add-and-search-word/
