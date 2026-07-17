class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        parent = [i for i in range(len(edges) + 1)]

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                parent[p2] = p1
                return True
            return False
            
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]