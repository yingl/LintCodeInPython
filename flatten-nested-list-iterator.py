"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = []
        self.pushToStack(nestedList)
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.stack.pop().getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.stack:
            tmp = self.stack[-1]
            if tmp.isInteger():
                return True
            else:
                tmp = self.stack.pop()
                self.pushToStack(tmp.getList())
        return False

    def pushToStack(self, nestedList):
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# medium: https://www.lintcode.com/problem/flatten-nested-list-iterator/
