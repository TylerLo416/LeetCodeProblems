class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (r+l)//2
        while l != r:
            if target < mid:
                r = mid
                mid = (l+r)/2
            elif target > mid:
                l = mid
                mid = (l+r)/2
            elif target == mid:
                return mid
        return -1
