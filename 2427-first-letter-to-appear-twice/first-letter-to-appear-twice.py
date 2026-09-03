class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        st = set()
        for i in s:
            if i in st:
                return i
            st.add(i)