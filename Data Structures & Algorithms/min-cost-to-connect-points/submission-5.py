class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit = set() # (x, y)
        minheap = [(0, (points[0][0], points[0][1]))] # (dist, (x0, y0))
        res = 0

        while len(visit) < len(points):
            dist, point = heapq.heappop(minheap)
            xi, yi = point[0], point[1]
            if (xi, yi) not in visit: 
                res += dist
                visit.add((xi, yi))

                for xj, yj in points:
                    if (xj, yj) not in visit:
                        manhattan = abs(xi - xj) + abs(yi - yj)
                        heapq.heappush(minheap, (manhattan, (xj, yj)))
        
        return res