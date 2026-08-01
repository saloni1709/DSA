class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        stack = []

        for ch in operations:            
            if ch == '+':
                stack.append(stack[-1] + stack[-2])
            elif ch == 'D':
                stack.append(stack[-1] * 2)
            elif ch == 'C':
                stack.pop()
            else:
                stack.append(int(ch))
        
        return sum(stack)