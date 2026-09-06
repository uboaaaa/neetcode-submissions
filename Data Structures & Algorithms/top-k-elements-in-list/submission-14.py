class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) # num -> freq
        for num in nums:
            counts[num] += 1
        
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (-freq, num))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
