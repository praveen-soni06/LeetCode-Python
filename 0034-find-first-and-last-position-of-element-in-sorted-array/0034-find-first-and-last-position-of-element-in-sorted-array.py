def binarySearch(nums, target, leftBais):
    s,e = 0, len(nums)-1
    i = -1
    while s<=e:
        mid = (s+e)//2
        if nums[mid] < target:
            s = mid + 1
        elif nums[mid] > target:
            e = mid - 1
        else:
            i = mid
            if leftBais:
                e = mid - 1
            else:
                s = mid + 1
    return i

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)

        return [left, right]