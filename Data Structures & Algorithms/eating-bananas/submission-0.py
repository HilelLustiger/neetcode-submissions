class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def func(piles: List[int], h: int, k: int) -> bool:
            counter = 0
            for i in range(len(piles)):
                counter += math.ceil(piles[i] / k)
            
            return counter <= h
        
        low, high = 1, max(piles)
        while low < high:
            mid = (high + low) // 2
            if func(piles, h, mid):
                high = mid
            else:
                low = mid + 1
            
        return low