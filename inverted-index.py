'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        r = {}
        for d in docs:
            for w in d.content.split(' '):
                if w:
                    if w not in r:
                        r[w] = [d.id]
                    elif r[w][-1] != (d.id):
                        r[w].append(d.id)
        return r
