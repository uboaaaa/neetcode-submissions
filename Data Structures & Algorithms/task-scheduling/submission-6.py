class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        heap = [[count, task] for task, count in Counter(tasks).items()] # [count, task]
        heapq.heapify_max(heap)
        q = collections.deque() # [task, count, cooldown]

        while heap or q:
            if heap:
                count, task = heapq.heappop_max(heap)
                res += 1
                count -= 1
                if count: q.append([task, count, res + n])
            else:
                res = q[0][2]
            
            if q and res == q[0][2]:
                task, count, _ = q.popleft()
                heapq.heappush_max(heap, [count, task])
        
        return res