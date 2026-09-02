class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        f = {}
        for i in nums:
            f[i] = f.get(i, 0) + 1
            if f[i] > 1:
                return True
        return False