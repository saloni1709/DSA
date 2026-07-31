class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        f1 = {}
        f2 = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in f1:
                if f1[c1] != c2:
                    return False
            else:
                f1[c1] = c2

            if c2 in f2:
                if f2[c2] != c1:
                    return False
            else:
                f2[c2] = c1
    
        return True
        
       
        
        