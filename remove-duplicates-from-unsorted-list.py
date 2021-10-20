"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here
        if head:
            s = set([head.val])
            node = head.next
            tail = head
            tail.next = None
            while node:
                if node.val not in s:
                    s.add(node.val)
                    tail.next = node
                    tail = node
                    node = node.next
                    tail.next = None
                else:
                    node = node.next
        return head
      
# easy: https://www.lintcode.com/problem/217/discuss
