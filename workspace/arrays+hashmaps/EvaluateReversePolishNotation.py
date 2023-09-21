class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #2 stacks, 1 for numbers, 1 for operators
        #pop a number as the starting number
        #pop an operator, than pop the next number off the stack and solve
        
        numbers = []
        operators = []

        for i in tokens:
            if(i == '+' or i == '-' or i == '*' or i == '/'):
                operators.append(i)
            else:
                numbers.append(i)
        
        currSum = numbers.pop()
        while len(operators) != 0:
            currOperator = operators.pop()
            if(currOperator == '+'):
                currSum = currSum + numbers.pop()
            elif currOperator == '-':
                currSum = currSum - numbers.pop()
            elif(currOperator == '*'):
                currSum = currSum * numbers.pop()
            elif currOperator == '/':
                currSum = currSum/numbers.pop()
        return currSum