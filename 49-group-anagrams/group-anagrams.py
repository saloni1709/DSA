class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        f = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in f:
                f[key] = []
            f[key].append(word)
        return list(f.values())