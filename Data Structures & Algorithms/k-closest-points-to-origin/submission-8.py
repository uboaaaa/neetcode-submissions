class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush_max(heap, [dist, x, y])
        
        while len(heap) > k:
            heapq.heappop_max(heap)
        
        return [[x,y] for dist, x, y in heap]