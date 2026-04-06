"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            #If node is already cloned in the dictionary, return clone
            if node in oldToNew:
                return oldToNew[node]
            
            #If node isn't cloned create a clone and add it to dictionary
            clone = Node(node.val)
            oldToNew[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        
        return dfs(node) if node else None



        