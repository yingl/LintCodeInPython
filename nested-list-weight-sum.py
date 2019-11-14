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


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    @staticmethod
    def _depthSum(nestedList, count, level=1): # 递归，level记录深度
        for i in nestedList:
            if i.isInteger():
                count[0] += i.getInteger() * level
            else:
                Solution._depthSum(i.getList(), count, level+1)
        
    def depthSum(self, nestedList):
        # Write your code here
        count = [0]
        Solution._depthSum(nestedList, count)
        return count[0]
        
# easy: https://www.lintcode.com/problem/nested-list-weight-sum
