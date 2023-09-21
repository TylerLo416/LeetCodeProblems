class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if map.get(i)==1:
                return True
            else:
                map[i] = 1
        return False