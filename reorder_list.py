# -*- coding: utf-8 -*-

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
            slow, fast = head, head # fast每次前进2步
            while fast:
                fast = fast.next
                if not fast:
                    break
                fast = fast.next
                slow = slow.next
                print slow.val, fast.val
            