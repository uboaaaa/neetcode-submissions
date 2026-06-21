class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        
        heap = []
        for num in hm.keys():
            heapq.heappush_max(heap, (hm[num], num))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])
        
        return res
