# coding: utf-8

class Solution:
    """
    @param: head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        ret = 0
        while head:
            ret += 1
            head = head.next
        return ret
        
# naive: http://lintcode.com/zh-cn/problem/count-linked-list-nodes/
