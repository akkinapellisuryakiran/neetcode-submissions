class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        components = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)

        for i, nodes in enumerate(graph):
            if i not in visited:
                components += 1
                dfs(i)
        return components