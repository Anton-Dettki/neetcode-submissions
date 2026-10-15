class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(float(p) / k)
            
            if hrs <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res