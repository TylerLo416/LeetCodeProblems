class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #set up binary search
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + ((r-l)//2)
            print(l,m,r)
            if r-l <= 1:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
            #if l and r < m, then iterate toward the direction of
            #the target, if target < m, then r = m -1, else l = m+1
            #if l and r > m, iterate toward direction of target
            if nums[m] == target:
                return m
            if ((target < nums[l] and target > nums[m] and target < nums[r]) or \
                (target > nums[l] and target > nums[m] and target < nums[r])):
                l = m+1
            elif ((target > nums[l] and target < nums[m] and target > nums[r]) or \
                  (target > nums[l] and target > nums[m] and target < nums[r])):
                r = m-1
            elif (target < nums[l] and target < nums[m] and target < nums[r]):
                if nums[m] > nums[r]:
                    l = m+1
                else:
                    r = m-1
            elif (target < nums[l] and target < nums[m] and target < nums[r]):
                if nums[m] > nums[r]:
                    l = m+1
                else:
                    r = m-1
            elif ((target > nums[l] and target > nums[m] and target > nums[r])):
                if nums[m] < nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
        return -1
            #big small reversed, then 
                #if target bigger than l but smaller than m, r = m-1

            #if any l, r, m = target, return that index

        #else return -1
