# coding: utf-8

class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    self.map = {} # 记录后序某个字母是否出现
    self.isLeaf = False

class Trie:
  def __init__(self):
    self.root = TrieNode()  # 根节点

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
    root = self.root
    for ch in word:
      if ch not in root.map:
          root.map[ch] = TrieNode() # ch出现并记录
      root = root.map[ch]
    root.isLeaf = True  # 该节点可以为叶子节点


  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
    root = self.root
    i = 0
    for ch in word:
      if ch not in root.map:  # 找不到匹配字符，直接返回False。
        return False
      else:
        i += 1
        if (i == len(word)) and root.map[ch].isLeaf:  # 判断是否最后一个字母且为叶子节点
          return True
        root = root.map[ch]
    return False
        

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
    root = self.root
    for ch in prefix:
      if ch not in root.map:
        return False
      else:
        root = root.map[ch]
    return True

# medium: http://lintcode.com/zh-cn/problem/implement-trie/
