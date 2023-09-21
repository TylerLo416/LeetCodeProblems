class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #add all to a set
        numSet = set(nums)
        largest = 0
        #check the set for the start of the sequence (does it have a consecutive number smaller),
        for i in set:
            curCount = 0
            if not i-1 in set:
        #check if it has a larger number
                while i+1 in set:
                    curCount += 1
                    i += 1
            if curCount > largest:
                largest = curCount
        return largest
