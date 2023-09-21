from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #add all to a hashmap, incrementing count
        #sort the outputted hashmap by putting it into an array, sorted by hashmap values (num of each elem)
        defdict = {}
        for i in nums:
            defdict[i] = 1+defdict.get(i,0)
        
        frequency = [[] for i in range(len(nums)+1)]
        
        for n, c in defdict.items():
            frequency[c].append(n)

        result = []
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                result.append(n)
                if len(result) is k:
                    return result
        return result