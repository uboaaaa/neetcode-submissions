class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        # now len(edges) == n - 1. need dfs to check whether there are island nodes and / or 
        # cycles
        # islands: if after dfs traversal len(visit) != n, return False
        # cycles: if while dfs traversing, we see a node in visit that isn't our parent, return False
        visit = set()
        adj = {x : [] for x in range(n)}
        flag = True

        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        
        def dfs(parent, node): # (parent, node) -> None
            nonlocal flag
            visit.add(node)

            for neigh in adj[node]:
                if neigh != parent:
                    if neigh in visit: 
                        flag = False
                    else:
                        dfs(node, neigh)


        dfs(-1, 0)
        if len(visit) != n:
            flag = False

        print(adj.items())
        return flag