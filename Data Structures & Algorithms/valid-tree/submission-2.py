class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        visit = set()
        adj = {x : [] for x in range(n)}
        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)

        def dfs(node):
            visit.add(node)
            for neigh in adj[node]:
                if neigh not in visit:
                    dfs(neigh)
        
        dfs(0)
        return len(visit) == n