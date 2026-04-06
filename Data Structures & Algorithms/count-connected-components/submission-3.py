class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        dfs through the first edge given
        mark all nodes connected as visited
        make an adjacency graph

        populate adjacency graph:
            for i in range(n):
                adjgraph[i] = []
            for node, nei in edges:
                adggraph[node].append(nei)
                adjgraph[nei].append(node)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neib in adjgraph[node]:
                dfs(neib)

        """
        visited = set()

        adjGraph = {}
        count = 0
        for i in range(n):
            adjGraph[i] = []
        for node, nei in edges:
            adjGraph[node].append(nei)
            adjGraph[nei].append(node)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neib in adjGraph[node]:
                dfs(neib)
        
        if n == 1:
            return 1

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count



        