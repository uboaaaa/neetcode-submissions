class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        openCounter = closeCounter = n

        def dfs(sub, openCounter, closeCounter):
            if openCounter == closeCounter == 0:
                res.append(sub)
                return

            if openCounter > 0:
                dfs(sub + "(", openCounter - 1, closeCounter)
            if closeCounter > openCounter:
                dfs(sub + ")", openCounter, closeCounter - 1)
            
        
        dfs("", openCounter, closeCounter)
        return res