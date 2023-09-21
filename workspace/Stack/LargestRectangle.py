class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #Stack, in increasing order
        stack = []
        maxArea = 0
        decrementIndex = 0
        #iterate through the height array
        for i, height in enumerate(heights):
            #if the height is bigger than the top of stack, add it to stack
            if height >= stack[-1]:
                #append index, height
                stack.append((i - decrementIndex,height))
                # reset index decrementer
                decrementIndex = 0
            #else, calculate the max area of the current top of the stack
            else:
                while(height > stack[-1]):
                    curHeight = stack.pop()
                    #use the height of the popped rectangle * index
                    if curHeight[0]*curHeight[1] > maxArea:
                        maxArea = curHeight[0]*curHeight[1]
                    decrementIndex += 1
        return maxArea