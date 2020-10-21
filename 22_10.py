# Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        res = Node(1,[])
        d = {}
        def dfs(node,res):
            d[node] = res
            for i in node.neighbors:
                if i not in d:
                    new = Node(i.val,[])
                    res.neighbors.append(new)
                    dfs(i,new)
                else:
                    res.neighbors.append(d[i])

        dfs(node,res)
        return res
