class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        fre = {}
        for i in nums:
            fre[i] = fre.get(i, 0) + 1
            if fre[i] > 1:
                return True
        return False
        