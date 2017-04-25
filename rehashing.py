# coding: utf-8

class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        old_size = len(hashTable)
        for i in xrange(old_size):
            hashTable.append(None)
        for i in xrange(old_size):
            prev, node = None, hashTable[i]
            while node:
                pos = node.val % (old_size * 2)
                if pos >= old_size: # 该元素需要分配到新的位置上
                    next_node = node.next # 先保留next节点
                    if not hashTable[pos]:
                        hashTable[pos] = node
                    else:
                        new_node = hashTable[pos]
                        while new_node:
                            if new_node.next:
                                new_node = new_node.next  # 插到新链表的尾部
                            else:
                                new_node.next = node
                                break
                    node.next = None
                    if not prev:
                       hashTable[i] = next_node
                    else:
                        prev.next = next_node
                    node = next_node 
                else:
                    prev = node
                    node = node.next
        return hashTable

# medium: http://lintcode.com/zh-cn/problem/rehashing/
