class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s1 = []
        s2 = []

        for i in s:
            if i == '#':
                if len(s1) > 0:
                    s1.pop()
            else:
                s1.append(i)

        for j in t:
            if j == '#':
                if len(s2) > 0:
                    s2.pop()
            else:
                s2.append(j)
        
        # if s1 == s2:
        #     return True
        # return False

        return s1 == s2
        