class Solution:
    def climbStairs(self, n: int) -> int:
        two_behind, one_behind = 1, 1
        for _ in range(2, n + 1):
            two_behind, one_behind = one_behind, two_behind + one_behind
        
        return one_behind