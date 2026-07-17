class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        res = 0
        adj = {x : [] for x in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set() # node ints

        def dfs(node):
            visit.add(node)
            for neigh in adj[node]:
                if neigh not in visit:
                    dfs(neigh)
        
        for node in range(n):
            if node not in visit:
                res += 1
                dfs(node)
        

        return res
