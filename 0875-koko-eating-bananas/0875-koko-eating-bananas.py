class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        res = float('inf')

        while s <= e:
            count = 0
            mid = s+(e-s)//2
            for i in range(len(piles)):
                temp = (piles[i] + mid - 1) // mid
                count += temp
                if count > h:
                    break
            if count <= h:
                res = min(res, mid)          
                e = mid - 1
            else:
                s = mid + 1

        return res