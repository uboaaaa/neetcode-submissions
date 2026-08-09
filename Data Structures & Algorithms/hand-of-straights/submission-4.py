class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 1, 2, 2, 3, 3, 4, 4, 5
        # 1, 2, 3, 4 STOP
        # 2 
        highest = max(hand)
        card_counts = [0] * (highest + 1)

        for num in hand:
            card_counts[num] += 1
        
        for i in range(len(card_counts)):
            while card_counts[i]:
                for j in range(i, i + groupSize):
                    if j < len(card_counts) and card_counts[j]:
                        card_counts[j] -= 1
                    else:
                        return False
                    

        
        return True

            