class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """

        only need to check one node
        dfs starting with node 0
        dfs(node):
            if node in visited return false
            if node has no neighbors thats not the parent node return true
            add node to visited
            dfs through neighbors

        """
        neiMap = {}
        for i in range(n):
            neiMap[i] = []
        
        for node, neib in edges:
            neiMap[node].append(neib)
            neiMap[neib].append(node)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            if neiMap[node] == [] or neiMap[node] == [parent]:
                return True

            
            for nei in neiMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        for node in range(n):
            if node not in visited:
                return False
        return True

        



        