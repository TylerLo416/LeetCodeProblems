class Solution:
    def maxArea(self, height: List[int]) -> int:
        #2 pointers, keep track of the index and the height at that index
        l = 0
        r = len(height)-1
        maxArea = 0
        #iterate through the entire array; find the area, and update maxarea
        while l < r:
            smallerBeam = min(height[l],height[r])
            if smallerBeam*(r-l) > maxArea:
                maxArea = smallerBeam
            if smallerBeam == height[l]:
                l += 1
            else:
                r -= 1
        return maxArea
            