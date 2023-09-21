class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #combine position, speed into one array. sort by position
        tupleCars = []
        stackOfCarFleets = [float('inf')]
        for i in range(len(position)-1,-1,-1):
            tupleCars.append((position[i],speed[i]),)

        #for loop to iterate starting from the right 
            for i in tupleCars:
        #calculate final time to reach destination. 
                curTime = (target-i[0])/i[1]
        #if final time is less than topOfStack's time to reach destination,
        #insert into stack
                if curTime < stackOfCarFleets[-1]:
                    stackOfCarFleets.append(curTime)
        #else if greater than / equal to, don't insert

        #return length of stack
        return len(stackOfCarFleets)