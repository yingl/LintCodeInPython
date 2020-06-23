"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head node
    @return: the middle node
    """
    def middleNode(self, head):
        # write your code here.
        # 添一个fake head方便统一处理
        fh = ListNode(0)
        fh.next = head
        slow, fast = fh, fh
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        return slow

# easy: https://www.lintcode.com/problem/middle-of-the-linked-list/
