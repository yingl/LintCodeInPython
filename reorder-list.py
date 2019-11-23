# coding: utf-8

class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        '''
        0->1->2->3->4->5 (n = 5) => 0->5->1->4->2->3 (012/543)
        0->1->2->3->4->5->6 (n = 6) => 0->6->1->5->2->4->3 (0123/654)
        '''
        if head:
            prev, slow, fast = None, head, head # fast每次前进2步
            while fast:
                prev = slow
                slow = slow.next
                fast = fast.next
                if not fast:
                    break
                fast = fast.next
            old_tail = prev
            old_tail.next = None
            new_head = slow
            new_head = self.reverse(new_head)
            while head:
                if new_head:
                    _next = head.next
                    head.next = new_head
                    new_head = new_head.next
                    head.next.next = _next
                    head = _next
                else:
                    head = head.next

    def reverse(self, head):
        # write your code here
        if not head:
            return None
        new_head = None
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        return new_head

# medium: http://lintcode.com/zh-cn/problem/reorder-list/
