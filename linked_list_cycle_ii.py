# coding: utf-8

class Solution:
    """
    @param head: The first node of the linked list.
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        # 先确定是否有环，然后确定环的大小，再遍历确定位置。
        cycle_len = -1
        one_node, two_node = head, head
        while two_node:
            for i in xrange(2):
                if two_node:
                    two_node = two_node.next
                    if two_node == one_node:
                        cycle_len = 1
                        two_node = one_node.next
                        while two_node != one_node: # 算出环的长度
                            cycle_len += 1
                            two_node = two_node.next
                        break
                else:
                    break
            one_node = one_node.next
            if (not two_node) or (cycle_len != -1):
                break
        if cycle_len == -1:
            return None
        one_node, two_node = head, head # two_node先前进的距离等于环的长度
        i = 0
        while i < cycle_len:
            two_node = two_node.next
            i += 1
        while one_node != two_node:
            one_node = one_node.next
            two_node = two_node.next
        return one_node

# hard: http://lintcode.com/zh-cn/problem/linked-list-cycle-ii/
