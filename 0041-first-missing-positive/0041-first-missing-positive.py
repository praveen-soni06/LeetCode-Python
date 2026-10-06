class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1

        for i in range(n):
            index = abs(nums[i])-1
            if index < n:
                nums[index] = -abs(nums[index])
            
        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1
