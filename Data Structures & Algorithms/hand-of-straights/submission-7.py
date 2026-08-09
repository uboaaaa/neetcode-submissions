class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hm = {}
        for num in hand:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
        
        hand.sort()
        for num in hand:
            if hm[num]:
                for i in range(num, num + groupSize):
                    if i not in hm or not hm[i]:
                        return False
                    hm[i] -= 1
        
        return True