class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seen = list(set(nums))
        seen.sort()
        if len(seen) < 3:
            return seen[-1]
        return seen[-3]