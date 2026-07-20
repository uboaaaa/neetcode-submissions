class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque([(0, src)]) # (cost, node)
        prices = [float('inf')] * n 
        prices[src] = 0

        adj = {x : [] for x in range(n)}
        for u, v, c in flights:
            if u not in adj:
                adj[u] = []
            adj[u].append((c, v))
        
        while q and k > -1:
            print(k)
            for _ in range(len(q)):
                cost, node = q.popleft()

                for neigh_cost, neigh in adj[node]:
                    cost_to_neigh = neigh_cost + cost
                    if cost_to_neigh < prices[neigh]:
                        prices[neigh] = cost_to_neigh
                        q.append((prices[neigh], neigh))
            
            k -= 1

        return prices[dst]if prices[dst] != float('inf') else -1
