from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #add all to a hashmap
        #iterate through the array
        #check hashmap if corresponding number exists in the hashmap
        allNums = {}

        for i, num in enumerate(nums):
            if target-num in allNums:
                return [i, allNums.get(target-num)]
            
            allNums[num] = i # value = key, index = element
            
            #check if corresponding value already exists
