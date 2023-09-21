class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 pointers, 
        # move the first until first plus second is too large
        #repeat
        first, second = 0,len(numbers)-1
        while first < second:
        #move the second until it plus first is smaller than target
            cur = numbers[first]+numbers[second]
            if cur == target:
                return [first,second]
            elif cur > target:
                first += 1
            elif cur < target:
                second -= 1
        return []

