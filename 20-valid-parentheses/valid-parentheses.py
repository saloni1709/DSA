class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        valid = True

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')' or ch == ']' or ch == '}':
                if len(stack) == 0:
                    valid = False
                    break
                if stack[-1] != pairs[ch]:
                    valid = False
                    break
                stack.pop()

        if valid and len(stack) == 0:
            return True
        else:
            return False