class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l = 0
        total = sum(nums)
        ans = []
        for i in range(len(nums)):
            r = total - l - nums[i]
            ans.append(abs(l-r))
            l += nums[i]
        return ans