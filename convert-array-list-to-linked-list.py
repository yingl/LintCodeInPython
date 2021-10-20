"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: nums: an integer array
    @return: the first node of linked list
    """
    def toLinkedList(self, nums):
        # write your code here
        head, tail = None, None
        for i in nums:
            if not head:
                head = ListNode(i)
                tail = head
            else:
                node = ListNode(i)
                tail.next = node
                tail = node
        return head
      
# easy: https://www.lintcode.com/problem/489
