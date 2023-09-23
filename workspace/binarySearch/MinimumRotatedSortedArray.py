class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minVal = float('inf')
        while l <= r:
            m = l + (r-l)//2
            if m < minVal:
                minVal = m
            
            if nums[m] < nums[l]:#check behind and ahead
                r = m-1
            elif nums[m] > nums[r]:
                l = m+1
        return minVal