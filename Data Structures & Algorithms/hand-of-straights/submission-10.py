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
                    if not hm.get(i, 0):
                        return False
                    hm[i] -= 1
        
        return True