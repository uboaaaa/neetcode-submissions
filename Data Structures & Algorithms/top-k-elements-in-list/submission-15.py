class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) # num -> freq
        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        res = []
        for freq in range(len(nums), 0, -1):
            if buckets[freq]:
                for num in buckets[freq]:
                    res.append(num)
                    if len(res) == k:
                        return res