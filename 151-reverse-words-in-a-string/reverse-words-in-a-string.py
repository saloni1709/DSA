class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # words = s.split()
        # s = words[::-1]
        # s = " ".join(s)

        # return s


        ## BY STACK
        stack = []
        ans = ""
        for word in s.split():
            stack.append(word)
        while stack:
            ans += stack.pop() + " "
        
        return ans.rstrip()