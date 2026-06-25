class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        merge = sorted(zip(position, speed), reverse=True)

        for elem in merge:
            time = (target - elem[0]) / elem[1]
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
