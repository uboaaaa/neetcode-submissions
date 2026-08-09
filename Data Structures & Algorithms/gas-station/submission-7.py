class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        res = 0
        tank = 0
        for i in range(len(gas)):
            # reset condition
            if tank + gas[i] < cost[i]:
                tank = 0
                res = i + 1
            else:
                tank += gas[i] - cost[i]
        
        return res