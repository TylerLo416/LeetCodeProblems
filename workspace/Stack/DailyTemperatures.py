class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Decreasing Monotonic Stack, the stack is always in decreasing order
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(i)
                continue
            while temp > temperatures[stack[-1]]:
                j = stack.pop()
                result[i] = i - j 
                
            stack.append(i)
        return result