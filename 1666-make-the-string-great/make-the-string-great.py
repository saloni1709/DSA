class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for ch in s:
            if stack:
                if stack[-1].lower() == ch.lower() and stack[-1] != ch:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        
        return "".join(stack)
        