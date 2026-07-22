class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        l = 0
        for r in nums:
            if r != val:
                nums[l] = r
                l += 1
        
        return l
        