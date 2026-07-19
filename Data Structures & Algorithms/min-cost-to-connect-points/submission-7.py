class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [10000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            
            for i in range(n):
                if visit[i]:
                    continue
                xi, yi = points[node]
                xj, yj = points[i]
                curDist = abs(xi - xj) + abs(yi - yj)
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
                
            res += dist[nextNode]
            node = nextNode
            edges += 1
        
        return res

                