class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)
        l = 0
        
        for i in range(len(nums)):
            curr = nums[i]
            r = total - l - curr
        
            if l == r:
                return i
            else:
                l += nums[i]
                i += 1
        
        return -1