# coding: utf-8

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        '''
        思路如下，abcd...代表原链表，a'b'c'd'...代表新链表。()内代表random，'/'代表None。
        初始状态：a(d)->b(/)->c(e)->d(a)
        1. 插入并复制原来的random节点：a(d)->a'(d)->b(/)->b'(/)->c(e)->c'(e)->d(a)->d'(a)
        2. 更新新节点的random（因为x指向x'）：a(d)->a'(d')->b(/)->b'(/)->c(e)->c'(e')->d(a)->d'(a')
        3. 拆成两条链表并返回
        '''
        if not head:
            return None
        node = head
        while node:
            new_node = RandomListNode(node.label)
            new_node.next, new_node.random = node.next, node.random
            node.next = new_node
            node = new_node.next
        node = head.next
        while node:
            node.random = node.random.next
            node = node.next  # 向前两步
            node = node.next
        new_head, new_tail = None, None
        node = head
        while node:
            prev = node
            node = node.next
            prev.next = node.next # prev.next保存下一个node的位置
            if not new_head:
                new_node = node
            else:
                new_tail.next = node
            new_tail = node
            new_tail.next = None
            node = prev.next
        return new_head

# medium: http://lintcode.com/zh-cn/problem/copy-list-with-random-pointer/
