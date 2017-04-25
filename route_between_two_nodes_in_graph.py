# coding: utf-8

class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        # 广度优先遍历
        nodes = [s]
        node_map = {s: True}
        pos = 0
        while pos < len(nodes):
            if nodes[pos] == t:
                return True
            for node in nodes[pos].neighbors:
                if node not in node_map:
                    node_map[node] = True
                    nodes.append(node)
            pos += 1
        return False

# medium: http://lintcode.com/zh-cn/problem/route-between-two-nodes-in-graph/
