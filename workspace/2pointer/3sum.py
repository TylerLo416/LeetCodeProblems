class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the list
        nums = nums.sort()
        soln = [[int]]
        #iterate through using a for loop to go to the next number.
        for i, addTo in enumerate(nums):
            #skip duplicates if already in soln
            if i > 0 and addTo == nums[i-1]:
                continue
            #do 2sum to add to the third number to equal 0
            first, second = i+1,len(nums)-1
            cur = first+second
            if cur+addTo == 0:
                soln.append([i,first+1,second+1])
            elif cur+addTo > 0:
                second -= 1
            else:
                first += 1
        return soln
