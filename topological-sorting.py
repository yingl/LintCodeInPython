# coding: utf-8

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        ret = []
        node_map = {}
        stack = []
        if graph:
            for node in graph:  # 更新指向节点的入度
                for neighbor in node.neighbors:
                    if neighbor not in node_map:
                        node_map[neighbor] = 1
                    else:
                        node_map[neighbor] += 1
            for node in graph:  # 找出入度为0的节点
                if node not in node_map:
                    stack.append(node)
            while stack:
                node = stack.pop()
                ret.append(node)
                for neighbor in node.neighbors: # 更新指向节点的入度
                    node_map[neighbor] -= 1
                    if node_map[neighbor] == 0:
                        stack.append(neighbor)
        return ret

# medium: http://lintcode.com/zh-cn/problem/topological-sorting/
