class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for u, v, t in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((v, t))
        
        minheap = [(0, k)] # (time, node)
        visit = {}
        while minheap:
            time, node = heapq.heappop(minheap)
            if node not in visit:
                visit[node] = time
            else:
                continue
            
            if node in adj:
                for neigh, newtime in adj[node]:
                    heapq.heappush(minheap, (newtime + time, neigh))

        

        return max(visit.values()) if len(visit) == n else -1





        