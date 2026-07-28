class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # nums = nums * 2
        # return nums


        ## By Linear Search

        ans = []

        for i in range(len(nums)):
            ans.append(nums[i])

        for i in range(len(nums)):
            ans.append(nums[i])

        return ans