"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        # write your code here
        odd_head, odd_tail = None, None # 奇偶分开再合并
        even_head, even_tail = None, None
        is_odd = True
        while head != None:
            node = head
            head = node.next
            node.next = None
            if is_odd:
                if odd_head is None:
                    odd_head = node
                    odd_tail = node
                else:
                    odd_tail.next = node
                    odd_tail = node
            else:
                if even_head is None:
                    even_head = node
                    even_tail = node
                else:
                    even_tail.next = node
                    even_tail = node
            is_odd = not is_odd
        if odd_head:
            odd_tail.next = even_head
            return odd_head
        else:
            return even_head

# medium: https://www.lintcode.com/problem/odd-even-linked-list
