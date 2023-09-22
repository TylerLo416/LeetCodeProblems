class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Find max number in piles
        #create array k from 1 to max(piles)
        #set up binary search through k
        max_piles = max(piles)
        l, r = 1, max_piles
        while l <= r:
            m = l + (r - l) // 2
            #for loop through piles[], check num hours required
            numHours = 0
            for i in piles:
                numHours += (i+m-1)//m
            #check until num hours is found
            if numHours > h:#k is too small, iterate up
                l = m+1
            elif numHours <= h:#k is too big, iterate down
                r = m-1
            else:
                return m
        return l