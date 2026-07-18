class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s,e = 0,len(nums)-1
        res = 0
        while s <= e:
            mid = s+(e-s)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                e = mid - 1
            else:
                s = mid + 1
                res = max(res, s)
                
        return res