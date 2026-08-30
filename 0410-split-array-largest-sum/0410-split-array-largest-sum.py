class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(largest):
            subarr = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarr += 1
                    curSum = n
            return subarr + 1 <= k

        s,e = max(nums), sum(nums)
        res = e
        while s <= e:
            m = s+((e-s)//2)
            if canSplit(m):
                res = m
                e = m - 1
            else:
                s = m + 1
        return res
        