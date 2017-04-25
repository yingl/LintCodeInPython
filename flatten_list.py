# coding: utf-8

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if not isinstance(nestedList, list):
            return [nestedList]
        return self._flatten([], nestedList)
        
    def _flatten(self, _list, nestedList):
        if isinstance(nestedList, list):
            for i in nestedList:
                if isinstance(i, list):
                    self._flatten(_list, i)
                else:
                    _list.append(i)
        return _list

# easy: http://lintcode.com/problem/flatten-list
